The first step is to install all our tools, so:

In a Linux terminal, we create the folder where the our project is supposed to be:

```
mkdir Pipeline
```

And, since we need python we need to install it, if you don't have it installed:

```python
sudo apt update

sudo apt install python3

sudo apt install python3-pip

sudo apt install python3-venv

python3 --version ## This is to check whether python was correctly installed
```

Once we have Python, we can create a virtual environment so that we won't have intersections between our libraries we already have installed, if that's the case. To create a python virtual  environment:

```
python3 -m vevn venv
```

Then, we need to put the project inside the virtual environment, such that:

```
source venv/bin/activate
```

Then, we can install our first tool, Airflow:

```bash
mkdir airflow

cd airflow

pip install apache-airflow

export AIRFLOW_HOME=$(pwd)

echo $AIRFLOW_HOME

airflow standalone

# (Ctr^C) to exit

cd .. # To get back to the main path of the project
```

In the first line, we're creating a new folder called "airflow" where i aimed to store all of the folders and files that airflow needs to work correctly. In the second line, i'm just entering to the folder. Then, in the third line, i'm installing the airflow library with the help of pip from python. Once is installed, we define a new environment variable "AIRFLOW_HOME" which the one that airflow uses to know where the dags are. The echo command is to print what's on the variable. And finally, once we have installed airflow, i initiate the airflow tool, the standalone ist ideal when we're beginners in the topic of airflow and basically initiates everything automatically, although we can initiate everython manually. In our web browser, we pass the "localhost:8080" url", so that we'll be able to access the GUI interface that airflow constructs for us (with flask). Then the user will be "admin" by default and the password will be stored in the "standalone_admin_password.txt" which was created at the time we executed the "ariflow standalone" command.

It's important to have in mind that you can do a bunch more of things like specifying a database and that sort of thing, but at least in this project i'll be working with the default configuration

The next step is to install kafka, so that we need to execute the following command:

```bash
sudo apt install default-jdk # In case you don't have installed Java

wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.12-3.9.0.tgz

tar -xzvf kafka_2.12-3.9.0.tgz

cd kafka_2.12-3.9.0

bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092

bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092

bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```

The first thing i do in the previous block of code, i install java, because kafka needs it to run. Then i download the file from the kafka website with the "wget" command help. Or you can just download it directly from their website: [Kafka](https://kafka.apache.org/). Then, since the folder is compressed, we need to descompress it, and that's what i do with the "tar" command where the "-xzvf" parameter stand for "x : Extract, z: Filter the archive through gzip, v : Verbose, f : Specifues the filename". Once decompressed the file,  i access to it, and first of running kafka itself; i need to run a Zookeeper environment which will help kafka in such a form i can't understand currently, anyway, that's the line in the nineth line. After that, we first create a topic where the messages are going to be stored and i can do that by executing the code in the eleventh line. Then, the only thing which is still missing is to write and read the messages, we'd be passing along the topic; that's the purpose of the last two written lines. The first one is to write messages and the second one is to read the messages, in this specific case the messages from the very beginning to the very end that's to say, from the first message ever created to the most current message.
