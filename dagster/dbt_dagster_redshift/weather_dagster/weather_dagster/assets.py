from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import dbt_dagster_project_project


@dbt_assets(manifest=dbt_dagster_project_project.manifest_path)
def dbt_dagster_project_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    