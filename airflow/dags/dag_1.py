from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from confluent_kafka import Producer
import mysql.connector, requests, logging

def kelvin_to_celsius(kelvin : float) -> float:
    return kelvin - 273.15

@task(task_id="SendMessage")
def SendMessage() -> None:
    conf : dict = {
        'bootstrap.servers':'localhost:9092'
    }
    p : Producer = Producer(conf)
    p.produce(topic = "airflow", value = "The data was gotten and sent succesfully!")
    p.flush()
    return "Done!"

@task(task_id = "WeatherAPI")
def WeatherAPI() -> dict:
    url = "https://api.openweathermap.org/data/3.0/onecall?lat=19.4326&lon=-99.1332&appid=7268c495c33b59fb722943fe931c8aa1"
    response  = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        data = data['current']
        logging.info("Data gotten succesfully!")
        return data
    else:
        return "Error!"
    
@task(task_id = "StoreData")
def StoreData(data : dict) -> None:
    config = {
        'host' : 'localhost',
        'user' : 'root',
        'password' : 'root',
        'port': 3306
    }

    with mysql.connector.connect(**config) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            dbs : list = [db[0] for db in cursor]
            anyWeather = any(map(lambda n : n == "Weather", dbs))
            if not anyWeather:
                logging.info(f"\n The database 'Weather' is not created yet!\n")
            elif anyWeather:
                cursor.execute("USE Weather;")

                cursor.execute("SHOW TABLES;")
                tabs : list = [tab[0] for tab in cursor]
                anyWeatherData = any(map(lambda n : n == "WeatherData", tabs))
                if not anyWeatherData:
                    logging.info(f"\n The table 'WeatherData' is not created yet!\n")
                elif anyWeatherData:
                    cursor.execute(f"""
                                        INSERT INTO Weather.WeatherData (Temperature_C, Pressure, Humidity, UVI, Visibility, WindSpeed, WindDegree)
                                        VALUES (%s{", %s" * 6})
                                        """, (kelvin_to_celsius(data['temp']), data['pressure'], data['humidity'], data['uvi'], data['visibility'], data['wind_speed'], data['wind_deg']))
                    logging.info("Data stored succesfully!")
        cnx.commit()


with DAG(
    dag_id="EtlWeather",
    start_date=datetime(2025, 2, 19),
    schedule = "@daily"
         ) as dag:
    weatherAPI = WeatherAPI()

    storeData = StoreData(weatherAPI)

    SendMessage = SendMessage()
