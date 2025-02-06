import os
from dagster import job, op, resource, Config, Definitions, RunRequest, RunConfig, sensor, SkipReason
from dagster_aws.s3 import S3Resource
from dagster_aws.redshift import RedshiftClientResource
from dagster_aws.s3.sensor import get_s3_keys

AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET", "weather-data-hatran")
AWS_S3_OBJECT_PREFIX = os.getenv("AWS_S3_OBJECT_PREFIX_Current", "output-data/Current_data/")

# Định nghĩa tài nguyên Redshift
@resource
def redshift_configured(context):
    return RedshiftClientResource(
        host=os.getenv("REDSHIFT_HOST"),
        port=int(os.getenv("REDSHIFT_PORT", 5439)),
        user=os.getenv("REDSHIFT_USER"),
        password=os.getenv("REDSHIFT_PASSWORD"),
        database=os.getenv("REDSHIFT_DATABASE", "dev"),
    )

# Định nghĩa tài nguyên S3
@resource
def s3_resource(context):
    return S3Resource(region_name=os.getenv("AWS_REGION", "ap-southeast-2"))

# Định nghĩa config cho ObjectConfig
class ObjectConfig(Config):
    key: str

# Định nghĩa op để chạy lệnh COPY từ S3 vào Redshift
@op(required_resource_keys={"s3", "redshift"})
def copy_s3_to_redshift(context, config: ObjectConfig):
    """
    Thực hiện lệnh COPY từ S3 vào Redshift.
    """
    s3_path = f"s3://{AWS_S3_BUCKET}/{config.key}"
    table_name = os.getenv("REDSHIFT_TABLE", "dev.public.weather_data")
    iam_role = os.getenv("IAM_ROLE_ARN")

    context.log.info(f"==================================={config.key}===================================")

    # Kết nối với Redshift thông qua tài nguyên redshift
    redshift_client = context.resources.redshift.get_client()

    copy_query = f"""
    COPY {table_name}
    FROM '{s3_path}'
    IAM_ROLE '{iam_role}'
    FORMAT AS PARQUET
    """

    redshift_client.execute_query(copy_query, fetch_results=True)
    context.log.info(f"Successfully copied data from {s3_path} to {table_name}")

# Định nghĩa tài nguyên config
@resource
def config_resource(context):
    return {
        "path": os.getenv("S3_FILE_PATH"),
        "table_name": os.getenv("REDSHIFT_TABLE"),
        "iam_role": os.getenv("IAM_ROLE_ARN")
    }

@job(resource_defs={
    "s3": s3_resource,
    "redshift": redshift_configured,
    "config": config_resource,
})
def s3_to_redshift_job():
    copy_s3_to_redshift()

@sensor(target=s3_to_redshift_job)
def S3_Current(context):
    latest_key = context.cursor or None
    unprocessed_object_keys = get_s3_keys(
        bucket=AWS_S3_BUCKET, prefix=AWS_S3_OBJECT_PREFIX, since_key=latest_key
    )

    # Lọc ra các file có đuôi `.parquet`
    parquet_files = [key for key in unprocessed_object_keys if key.endswith(".parquet")]

    for key in parquet_files:
        # Tạo một đối tượng config cho file S3 vừa phát hiện
        config = ObjectConfig(key=key)
        
        # Tạo RunRequest để gọi op copy_s3_to_redshift với config mới
        yield RunRequest(
            run_key=key, 
            run_config=RunConfig(ops={"copy_s3_to_redshift": config})
        )

    if not parquet_files:
        return SkipReason("No new .parquet files found in S3.")

    # Cập nhật cursor với file cuối cùng đã xử lý
    last_key = parquet_files[-1]
    context.update_cursor(last_key)


# Định nghĩa Definitions cho pipeline
defs = Definitions(
    resources={
        "s3": s3_resource,
        "redshift": redshift_configured,
        "config": config_resource,
    },
    sensors=[S3_Current],
)
