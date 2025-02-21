echo -e "\n"
export AIRFLOW_HOME=$(pwd)
echo "AIRFLOW_HOME: $AIRFLOW_HOME"
echo -e "\n"

export AIRFLOW_DATABASE_SQL_ALCHEMY_CONN="mysql+mysqlconnector://root:root@localhots:3306/Weather"
echo "AIRFLOW_DATABASE_SQL_ALCHEMY_CONN : $AIRFLOW_DATABASE_SQL_ALCHEMY_CONN"
echo -e "\n"

export AIRFLOW_EXECUTOR=SequentialExecutor
echo "AIRFLOW_EXECUTOR: $AIRFLOW_EXECUTOR"
echo -e "\n"

echo "You've declared all the environment varibales succesfully"
echo -e "\n"