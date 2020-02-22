from kafka import KafkaConsumer
import logging
from .models import Note
import time
import sys
logger = logging.getLogger(__name__)

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('user_alert',
                         group_id='None',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    print (message)