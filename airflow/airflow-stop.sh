echo -e "\n"

echo "Stopping Airflow"

pkill -f "airflow scheduler"
pkill -f "airflow webserver"

echo "Airflow has been stopped"

echo -e "\n"