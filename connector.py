import requests
import json
from confluent_kafka import Consumer, KafkaException

def source_postgres_connector(filename):
    # Load configuration from JSON file
    with open(filename, 'r') as file:
        connector_config = json.load(file)

    # Kafka Connect REST API URL
    url = 'http://localhost:8083/connectors'

    # Send POST request to create the connector
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(connector_config))

    # Check response status
    if response.status_code == 201:
        print(f"Connector {connector_config['name']} created successfully.")
    else:
        print(f"Failed to create connector: {response.text}")

