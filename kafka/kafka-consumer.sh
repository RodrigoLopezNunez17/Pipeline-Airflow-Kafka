echo -e "\n"
echo "Starting Kafka Consumer..."
echo -e "\n"
echo "Here are all of the messages from the 'airflow' topic:"
echo -e "\n"

kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic airflow --from-beginning