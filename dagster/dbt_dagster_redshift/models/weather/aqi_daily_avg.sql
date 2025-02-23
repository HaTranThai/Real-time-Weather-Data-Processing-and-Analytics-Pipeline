-- models/aqi_daily_avg.sql
SELECT
    a.coord_lat,
    a.coord_lon,
    DATE_TRUNC('day', TO_TIMESTAMP(a.dt::text, 'YYYY-MM-DD HH24:MI:SS')) AS day,  -- chuyển dt thành timestamp
    AVG(a.list_main_aqi) AS avg_aqi,
    AVG(a.list_components_co) AS avg_co,
    AVG(a.list_components_no) AS avg_no,
    AVG(a.list_components_no2) AS avg_no2,
    AVG(a.list_components_o3) AS avg_o3,
    AVG(a.list_components_so2) AS avg_so2,
    AVG(a.list_components_pm2_5) AS avg_pm2_5,
    AVG(a.list_components_pm10) AS avg_pm10,
    AVG(a.list_components_nh3) AS avg_nh3
FROM {{ ref('aqi_data') }} a
GROUP BY
    a.coord_lat,
    a.coord_lon,
    day 
