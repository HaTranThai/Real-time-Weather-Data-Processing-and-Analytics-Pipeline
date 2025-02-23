-- models/bad_aqi_locations.sql
SELECT
    w.coord_lat,
    w.coord_lon,
    w.weather_id,
    w.weather_main,
    w.temp,
    a.list_main_aqi
FROM {{ ref('weather_data') }} w
JOIN {{ ref('aqi_data') }} a
    ON w.coord_lat = a.coord_lat
    AND w.coord_lon = a.coord_lon
WHERE a.list_main_aqi > 2
