# Installing the required packages
sudo apt-get update

# sudo apt-get install default-libmysqlclient-dev build-essential
# pip install mysqlclient
# sudo apt-get install pkg-config libmysqlclient-dev

# Setting up all of the necessary services

python MySQL/CreateDB.py


# First of all, i need to initialize the airflow server

source venv/bin/activate
source airflow/airflow-start.sh

# Then i need to initialize the kakfka server so that i need to initialize the zookeeper server first

cd kafka
bin/zookeeper-server-start.sh config/zookeeper.properties --daemon
bin/kafka-server-start.sh config/server.properties --deamon
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic airflow --from-beginning