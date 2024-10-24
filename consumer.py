from confluent_kafka import Consumer, KafkaException

consumer_conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your broker's address
    'group.id': 'my_group',                # Consumer group ID
    'auto.offset.reset': 'earliest'        # Start reading from the earliest offset
}

def read_topic(topic_name):
    # Create a Consumer instance
    consumer = Consumer(consumer_conf)

    # Subscribe to the topic where PostgreSQL data is published
    topic = topic_name
    consumer.subscribe([topic])

    # Poll for new messages
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
        
            if msg is None:
                continue
        
            if msg.error():
                raise KafkaException(msg.error())
        
            # Process the message (e.g., print the value)
            print(f"Received message: {msg.value().decode('utf-8')}")
        
    except KeyboardInterrupt:
        print("Aborted by user")
    finally:
        # Close the consumer to ensure a graceful shutdown
        consumer.close()


def main():
    topic_name = "postgres_WORKERS"
    read_topic(topic_name)
    

if __name__ == "__main__":
    main()