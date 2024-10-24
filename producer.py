from confluent_kafka import Producer, avro
from confluent_kafka.admin import AdminClient, NewTopic
import json
from confluent_kafka.avro import AvroProducer
from connector import source_postgres_connector

def create_schema(filename):
    # Load the Avro schema from the file
    with open(filename, 'r') as f:
        schema_str = f.read()

    # Parse the schema
    value_schema = avro.loads(schema_str)

    return value_schema


# Kafka and Schema Registry configurations
producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://localhost:8081'
}


# Replication factor is number of copies, partition number is how many pieces the data is split into
def create_topic(topic_name, num_partitions, replication_factor):
    admin_client = AdminClient(producer_config)
    created_topic = NewTopic(topic_name, num_partitions, replication_factor)
    fs = admin_client.create_topics([created_topic])

    for topic, f in fs.items():
        try:
            f.result()  # Block until the topic creation is complete
            print(f"Topic '{topic}' created successfully.")
        except Exception as e:
            print(f"Failed to create topic '{topic}': {e}")


# If producer process fails, it runs this function
def delivery_report(error, message):
    if error is not None:
        print(f"Message delivery failed: {error}")
    else:
        print(f"Message delivered to {message.topic()} [{message.partition()}]")


# Pushing data to a topic via producer
def push_data(data, topic, schema_name):
    value_schema = create_schema(schema_name) # Creating schema

    producer = AvroProducer(
        producer_config,
        default_value_schema=value_schema # Putting schema into producer
    )

    for line in data:
        json_data = json.dumps(line)
        producer.produce(topic, value=json_data, callback=delivery_report)

    producer.flush()



def main():
    # Connects Postgresql via Kafka Connect
    filename = 'postgres_source_connect.json'
    source_postgres_connector(filename)

    # Pushing sample data to created topic
    data = [
        {"workerid": 1, "workername": "Alice Smith", "department": "HR", "salary": 50000, "city": "London"},
        {"workerid": 2, "workername": "Bob Johnson", "department": "Marketing", "salary": 55000, "city": "London"}
    ]

    topic_name = 'postgres_WORKERS'
    schema_file = 'schema_workers.avro'

    #create_topic("postgres_WORKERS", 3, 1)
    push_data(data, topic_name, schema_file)
    

if __name__ == "__main__":
    main()

