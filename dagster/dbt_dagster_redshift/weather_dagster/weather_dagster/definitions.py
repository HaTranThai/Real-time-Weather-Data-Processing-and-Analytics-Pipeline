from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import dbt_dagster_project_dbt_assets
from .project import dbt_dagster_project_project
from .schedules import schedules
from .S3_to_Redshift_sensor import S3_Current, S3_Pollution
from .extract_job import etl_job
from .extract_sensor import weather_api_sensor
from .create_table_job import create_redshift_tables

defs = Definitions(
    assets=[dbt_dagster_project_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=dbt_dagster_project_project),
    },
    sensors=[S3_Pollution, S3_Current, weather_api_sensor],
    jobs=[etl_job, create_redshift_tables],
)