kafka/bin/zookeeper-server-stop.sh config/zookeeper.properties
echo -e "\n"
echo "Zookeeper has been stopped"
echo -e "\n"

kafka/bin/kafka-server-stop.sh config/server.properties
echo "Kafka has been stopped"
echo -e "\n"