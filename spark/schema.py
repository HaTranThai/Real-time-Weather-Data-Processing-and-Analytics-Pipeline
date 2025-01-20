from pyspark.sql.types import (
    IntegerType, StringType, DoubleType, StructField, StructType, LongType, BooleanType, ArrayType
)

schema = {
    'Current_data' : StructType([
        StructField("coord", StructType([
            StructField("lon", DoubleType(), True),
            StructField("lat", DoubleType(), True)
        ]), True),
        StructField("weather", ArrayType(StructType([
            StructField("id", IntegerType(), True),
            StructField("main", StringType(), True),
            StructField("description", StringType(), True),
            StructField("icon", StringType(), True)
        ])), True),
        StructField("base", StringType(), True),
        StructField("main", StructType([
            StructField("temp", DoubleType(), True),
            StructField("feels_like", DoubleType(), True),
            StructField("temp_min", DoubleType(), True),
            StructField("temp_max", DoubleType(), True),
            StructField("pressure", IntegerType(), True),
            StructField("humidity", IntegerType(), True),
            StructField("sea_level", IntegerType(), True),
            StructField("grnd_level", IntegerType(), True)
        ]), True),
        StructField("visibility", IntegerType(), True),
        StructField("wind", StructType([
            StructField("speed", DoubleType(), True),
            StructField("deg", IntegerType(), True),
            StructField("gust", DoubleType(), True)
        ]), True),
        StructField("clouds", StructType([
            StructField("all", IntegerType(), True)
        ]), True),
        StructField("dt", LongType(), True),
        StructField("sys", StructType([
            StructField("country", StringType(), True),
            StructField("sunrise", LongType(), True),
            StructField("sunset", LongType(), True)
        ]), True),
        StructField("timezone", IntegerType(), True),
        StructField("id", LongType(), True),
        StructField("name", StringType(), True),
        StructField("cod", IntegerType(), True)
    ]),
    'Air_pollution_data' : StructType([
        StructField("coord", StructType([
            StructField("lon", DoubleType(), True),
            StructField("lat", DoubleType(), True)
        ]), True),
        StructField("list", ArrayType(StructType([
            StructField("main", StructType([
                StructField("aqi", IntegerType(), True)
            ]), True),
            StructField("components", StructType([
                StructField("co", DoubleType(), True),
                StructField("no", DoubleType(), True),
                StructField("no2", DoubleType(), True),
                StructField("o3", DoubleType(), True),
                StructField("so2", DoubleType(), True),
                StructField("pm2_5", DoubleType(), True),
                StructField("pm10", DoubleType(), True),
                StructField("nh3", DoubleType(), True)
            ]), True),
            StructField("dt", LongType(), True)
        ])), True)
    ])
}

