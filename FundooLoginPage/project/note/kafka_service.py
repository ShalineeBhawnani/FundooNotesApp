from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from .constants import KAFKA_BROKER_URL

import json

KAFKA_PRODUCER = None
def get_kafka_producer():
    KAFKA_PRODUCER = init_kafka_producer_instance()
    return KAFKA_PRODUCER

def init_kafka_producer_instance():
    try:

        if KAFKA_PRODUCER is not None :
            return KAFKA_PRODUCER

        producer = None
        producer = KafkaProducer(bootstrap_servers=[
                                 KAFKA_BROKER_URL], value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        return producer
    except Exception as e:
        import traceback
        print(traceback.format_exc())
    return None

def create_kafka_topic_instance(topic_name,num_partitions=1,replication_factor=1) :
    try :
        if topic_name is None :
            raise Exception("Invalid argument topic name")
        topic_list = []
        topic_list.append(NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor))
        create_topic(topic_list)
    except Exception as e :
        import traceback
        print(traceback.format_exc())

def create_topic(topics,validate_only=False):
    try:
        if topics is None:
            raise Exception("Topic is None")
        admin_client = get_kafka_admin_instance()
        if admin_client is None:
            return False
        result = admin_client.create_topics(topics,validate_only)
        print(result)
    except Exception as e:
        import traceback
        print(traceback.format_exc())


def get_kafka_admin_instance():
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKER_URL)
        return admin_client
    except Exception as e:
        import traceback
        print(traceback.format_exc())


def send_message(topic, json_data):
    try:
        if topic is None or json_data is None:
            raise Exception("Invalid argument topic or data")
        producer = get_kafka_producer()
        if producer is not None:
            x = producer.send(topic, json_data)
            print(x)
    except Exception as e:
        import traceback
        print(traceback.format_exc())


def delete_topic(topic):
    try:
        if topic is None:
            raise Exception("Topic is None")
    except Exception as e:
        import traceback
        print(traceback.format_exc())


def create_kafka_topic_name(obj) :
    try :
        if offering is None :
            raise Exception("Invalid argument offering, unable to create topic name")
        return str(obj.order_id)
    except Exception as e :
        print(e)
    return None