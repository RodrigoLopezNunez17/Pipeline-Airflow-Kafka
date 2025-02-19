from confluent_kafka import Producer
from datetime import datetime
from airflow import DAG
from airflow.decorators import task

conf = {
    "bootstrap.servers" : "localhost:9092"
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

@task(task_id="Firsttask")
def WeatherAPI():
    print(f"Current Time : {datetime.now()}")
    currenttime = datetime.now()
    producer.produce(f"Current time {currenttime}")
    producer.flush()
    return "Done"

with DAG(
    dag_id="FirstDAG",
    start_date = datetime(2025, 2, 18),
    schedule_interval = "*/5 * * * *"
) as dag:
    weatherTask = WeatherAPI()