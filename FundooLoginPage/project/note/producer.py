from kafka import KafkaProducer
import logging
from .models import Note
import time
import sys
logger = logging.getLogger(__name__)

#A Kafka client that publishes records to the Kafka cluster
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('user_alert', b'Hello, World!')
#producer.send(self, topic, value=None, key=None, headers=None, partition=None, timestamp_ms=None):

producer.flush()