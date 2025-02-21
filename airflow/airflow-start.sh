echo -e "\n"

echo "Starting Airflow"

airflow db migrate
airflow webserver -D
airflow scheduler -D

echo "Airflow has been started"

echo -e "\n"