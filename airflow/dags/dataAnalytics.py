from airflow import DAG
from datetime import datetime
from airflow.decorators import task

@task(task_id = "GettingData")
def GettingData():
    return None

@task(task_id = "Analysis")
def Analysis():
    return None

with DAG(
    dag_id = "DataAnalysis",
    description = "Here, i'll be analyzing the gathered data.",
    start_date = datetime(2025, 2, 19),
    schedule = "@weekly"
) as dag:
    GettingData()

    Analysis()