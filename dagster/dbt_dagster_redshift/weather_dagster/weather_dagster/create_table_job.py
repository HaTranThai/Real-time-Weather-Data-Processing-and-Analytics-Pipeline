from dagster import op, job, resource, Field, Output, In, Config
import psycopg2
from psycopg2 import OperationalError
import os

@op()
def create_table(context):
    try:
        conn = psycopg2.connect(
            dbname="dev",
            user=os.environ.get("REDSHIFT_USER"),
            password=os.environ.get("REDSHIFT_PASSWORD"), 
            host=os.environ.get("REDSHIFT_HOST"), 
            port="5439" 
        )

        cursor = conn.cursor()

        create_air_quality_data_table_query = """
        CREATE TABLE IF NOT EXISTS air_quality_data (
            coord_lat DOUBLE PRECISION,
            coord_lon DOUBLE PRECISION,
            list_main_aqi INTEGER,
            list_components_co DOUBLE PRECISION,
            list_components_no DOUBLE PRECISION,
            list_components_no2 DOUBLE PRECISION,
            list_components_o3 DOUBLE PRECISION,
            list_components_so2 DOUBLE PRECISION,
            list_components_pm2_5 DOUBLE PRECISION,
            list_components_pm10 DOUBLE PRECISION,
            list_components_nh3 DOUBLE PRECISION,
            dt TIMESTAMP
        );
        """
        cursor.execute(create_air_quality_data_table_query)

        create_weather_data_table_query = """
        CREATE TABLE IF NOT EXISTS weather_data (
            coord_lat DOUBLE PRECISION,
            coord_lon DOUBLE PRECISION,
            weather_id INT,
            weather_main VARCHAR(255),
            weather_description VARCHAR(255),
            weather_icon VARCHAR(255),
            base VARCHAR(255),
            temp DOUBLE PRECISION,
            feels_like DOUBLE PRECISION,
            temp_min DOUBLE PRECISION,
            temp_max DOUBLE PRECISION,
            pressure INT,
            humidity INT,
            sea_level INT,
            grnd_level INT,
            visibility INT,
            wind_speed DOUBLE PRECISION,
            wind_deg INT,
            wind_gust DOUBLE PRECISION,
            clouds_all INT,
            dt TIMESTAMP,
            country VARCHAR(255),
            sunrise TIMESTAMP,
            sunset TIMESTAMP,
            timezone INT,
            id BIGINT,
            name VARCHAR(255)
        );
        """
        cursor.execute(create_weather_data_table_query)

        conn.commit()
        context.log.info(f"Bảng đã được tạo thành công!")
        cursor.close()
        conn.close()

    except OperationalError as e:
        print(f"Không thể kết nối đến Redshift: {e}")

@job
def create_redshift_tables():
    create_table()