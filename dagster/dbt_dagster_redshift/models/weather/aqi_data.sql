-- model/aqi_data.sql
SELECT
    coord_lat,
    coord_lon,
    list_main_aqi,
    list_components_co,
    list_components_no,
    list_components_no2,
    list_components_o3,
    list_components_so2,
    list_components_pm2_5,
    list_components_pm10,
    list_components_nh3,
    dt
FROM air_quality_data