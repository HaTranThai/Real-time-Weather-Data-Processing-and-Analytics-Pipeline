from setuptools import find_packages, setup

setup(
    name="weather_dagster",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "weather_dagster": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-postgres<1.10",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)