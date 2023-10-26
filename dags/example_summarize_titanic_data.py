"""
example_summarize_titanic_data
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
from astro.table import Table, Metadata
import pandas as pd
import pendulum

import numpy
print('abc')

"""
This pipeline demonstrates how to use the Astro Cloud IDE. It loads the Titanic dataset, filters out passengers under 18, and aggregates the data by survival and class.

The pipeline is composed of four cells:

`load`: Loads the Titanic dataset from Seaborn's GitHub repository.

`over_18`: Filters out passengers under 18.

`aggregate_sql`: Aggregates the data by survival and class, using SQL.

`aggregate_python`: Aggregates the data by survival and class, using Python.

Note that each cell returns a value that can be referenced in subsequent cells using the `{{cell_name}}` syntax in SQL and `cell_name` syntax in Python.
"""

@aql.dataframe(task_id="load")
def load_func():
    import pandas as pd
    
    # use pandas to load the titanic dataset from github
    print('hello world')
    return pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

@aql.run_raw_sql(conn_id="duckdb_default", task_id="over_18", results_format="pandas_dataframe")
def over_18_func(load: Table):
    return """
    -- use SQL to filter out passengers under 18
    -- note that we can reference the output of the load cell using the {{load}} syntax
    SELECT *
    FROM {{load}}
    WHERE age > 18
    """

@aql.run_raw_sql(conn_id="duckdb_default", task_id="aggregate_sql", results_format="pandas_dataframe")
def aggregate_sql_func(over_18: Table):
    return """
    -- use SQL to calculate the average age and count of passengers by survival and class
    SELECT
        alive,
        class,
        avg(age) as avg_age,
        count(*) as count
    FROM {{ over_18 }}
    GROUP BY alive, class
    """

@aql.run_raw_sql(conn_id="duckdb_default", task_id="sql_1", results_format="pandas_dataframe")
def sql_1_func():
    return """
    select 'hello world'
    """

default_args={
    "owner": "Zed Zhou,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule=None,
    start_date=pendulum.from_format("2023-10-26", "YYYY-MM-DD"),
    catchup=False,
    owner_links={
        "Zed Zhou": "mailto:imzedbez@gmail.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/clo46s6a101jk01nbic9a3nd3/cloud-ide/clo4833qa007v01nuh15cni1s/clo4834ca01k001nbgsyev4ar",
    },
)
def example_summarize_titanic_data():
    load = load_func()

    over_18 = over_18_func(
        load,
    )

    aggregate_sql = aggregate_sql_func(
        over_18,
    )

    sql_1 = sql_1_func()

dag_obj = example_summarize_titanic_data()
