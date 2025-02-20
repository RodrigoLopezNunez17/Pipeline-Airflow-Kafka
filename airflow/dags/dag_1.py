from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from confluent_kafka import Producer

@task(task_id="send_message")
def send_message():
    conf = {
        'bootstrap.servers':'localhost:9092'
    }
    p = Producer(conf)
    p.produce(topic = "quickstart-events", value = f"The current time is : {datetime.now()}")
    p.flush()
    return "Done!"

with DAG(
    dag_id="DAG_1",
    start_date=datetime(2025, 2, 19),
    schedule_interval=timedelta(seconds = 30),
         ) as dag:
    send_message()
    print("DAG_1 is ready!")