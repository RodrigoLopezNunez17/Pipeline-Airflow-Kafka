kafka/bin/zookeeper-server-start.sh -daemon kafka/config/zookeeper.properties

echo -e "\n"
echo "Zookeeper has been started"
echo -e "\n"

sleep 5

kafka/bin/kafka-server-start.sh -daemon kafka/config/server.properties
echo "Kafka has been started"
echo -e "\n"