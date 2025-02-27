echo -e "\n"

echo "Starting Airflow"

source airflow/airflowEnvVar.sh
airflow db migrate
airflow webserver -D
airflow scheduler -D

echo -e "\n"
echo "Checking for the users"
echo airflow users list

if ! airflow users list | grep -q "IMNOTROY"; then
    airflow users create \
        --username "IMNOTROY" \
        --firstname "Rodrigo" \
        --lastname "López Núñez" \
        --role "Admin" \
        --email "notroylopnun@gmail.com"
else
    echo "User 'IMNOTROY' already exists!"
fi

echo -e "\n"

echo "Airflow has been started"

echo -e "\n"