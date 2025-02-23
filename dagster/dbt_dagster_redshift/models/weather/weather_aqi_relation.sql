-- models/weather_aqi_relation.sql
SELECT
    w.coord_lat,
    w.coord_lon,
    w.temp AS temperature,
    a.list_main_aqi AS aqi
FROM {{ ref('weather_data') }} w
JOIN {{ ref('aqi_data') }} a
    ON w.coord_lat = a.coord_lat
    AND w.coord_lon = a.coord_lon
WHERE w.temp IS NOT NULL
  AND a.list_main_aqi IS NOT NULL
