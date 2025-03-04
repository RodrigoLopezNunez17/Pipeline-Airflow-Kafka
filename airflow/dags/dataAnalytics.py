from airflow import DAG
from datetime import datetime
from airflow.decorators import task
import mysql.connector, subprocess
from io import StringIO

@task(task_id = "GettingData")
def GettingData():
    config : dict = {
        'user' : 'root',
        'password' : 'root',
        'host' : 'localhost',
        'port' : 3306
    }

    with mysql.connector.connect(**config, database = "Weather") as cnx:
        with cnx.cursor() as cursor:
            cursor.execute("""
                            SELECT *
                           FROM WeatherData;
                            """)
    return None

@task(task_id = "Analysis")
def Analysis():
    return None

with DAG(
    dag_id = "DataAnalysis",
    description = "Here, i'll be analyzing the gathered data.",
    start_date = datetime(2025, 2, 19),
    schedule = "@weekly",
) as dag:
    GettingData()

    Analysis()