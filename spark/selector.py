from pyspark.sql.functions import col, expr

def current_select(df):
    flat_df = df.select(
        col("coord.lat").alias("coord.lat"),
        col("coord.lon").alias("coord.lon"),
        col("weather").getItem(0).getField("id").alias("weather.id"),
        col("weather").getItem(0).getField("main").alias("weather.main"),
        col("weather").getItem(0).getField("description").alias("weather.description"),
        col("weather").getItem(0).getField("icon").alias("weather.icon"),
        col("base"),
        col("main.temp").alias("main.temp"),
        col("main.feels_like").alias("main.feels_like"),
        col("main.temp_min").alias("main.temp_min"),
        col("main.temp_max").alias("main.temp_max"),
        col("main.pressure").alias("main.pressure"),
        col("main.humidity").alias("main.humidity"),
        col("main.sea_level").alias("main.sea_level"),
        col("main.grnd_level").alias("main.grnd_level"),
        col("visibility"),
        col("wind.speed").alias("wind.speed"),
        col("wind.deg").alias("wind.deg"),
        col("wind.gust").alias("wind.gust"),
        col("clouds.all").alias("clouds.all"),
        col("dt"),
        col("sys.country").alias("country"),
        col("sys.sunrise").alias("sunrise"),
        col("sys.sunset").alias("sunset"),
        col("timezone"),
        col("id"),
        col("name"),
    )
    return flat_df

def airpollution_select(df):
    flat_df = df.select(
        col("coord.lat").alias("coord.lat"),
        col("coord.lon").alias("coord.lon"),
        col("list.main.aqi").getItem(0).alias("list.main.aqi"),
        col("list.components.co").getItem(0).alias("list.components.co"),
        col("list.components.no").getItem(0).alias("list.components.no"),
        col("list.components.no2").getItem(0).alias("list.components.no2"),
        col("list.components.o3").getItem(0).alias("list.components.o3"),
        col("list.components.so2").getItem(0).alias("list.components.so2"),
        col("list.components.pm2_5").getItem(0).alias("list.components.pm2_5"),
        col("list.components.pm10").getItem(0).alias("list.components.pm10"),
        col("list.components.nh3").getItem(0).alias("list.components.nh3"),
        col("list.dt").getItem(0).alias("dt")
    )
    return flat_df
