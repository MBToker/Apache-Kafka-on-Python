# Apache Kafka on Python
## 1) Description
In this project, we use Apache Kafka on Windows, using Python. Using functionalities of Kafka like: Kafka Connect, Kafka Schemas, ksqlDB, Producer and Consumer.

### 1.1) Technologies Used
Normally, Apache Kafka doesn't run on Windows. In order to run Apache Kafka on Windows, I downloadeded Confluent Platform on WSL and Ubuntu LTS. 
<br>WSL is a Linux command tool that can use Windows file system.
<br>Ubuntu LTS is an open source Linux distribution.

## 2) How to Install and Run The Project
*To activate WSL, write this line on Power Shell in administrator mode: **Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux**
<br>*Install Ubuntu LTS via Microsoft Store
<br>*After installation, open Ubuntu LTS and write rest of the lines.
<br>*To install Confluent Platform write this command: **wget https://packages.confluent.io/archive/6.1/confluent-6.1.0.tar.gz**
<br>*After the download process, extract the .tar file: **tar -xvf confluent-6.1.0.tar.gz**
<br>*After the extraction, enter the paths for Ubuntu to run Confluent Platform: **export CONFLUENT_HOME=~/confluent-6.1.0** and **export PATH=$CONFLUENT_HOME/bin:$PATH**
<br>*Install Datagen Connector with Confluent Hub: **confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:latest**
<br>*To start all of the services, enter this command: **confluent local services start**

## 3) Which File Used Where?
***connector.py:** contains the function that allows Kafka to create connector. In this project, it creates postgresql source connection. This function gets imported to producer.py.
<br>***postgres_source_connect.json:** file that contains the information that is going to be used in the creation of the connector. This file gets read by connector.py.
<br>***producer.py:** file that contains functionalities of creating topics, pushing data to topics, creating connector, creating and using schema.
<br>***schema_workers.avro:** file that contains the information of schema. Gives information about data's format.
<br>***consumer.py:** file that contains the functionalities of getting the data from topics

























