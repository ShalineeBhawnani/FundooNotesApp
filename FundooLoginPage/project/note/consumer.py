from kafka import KafkaConsumer
import datetime
import logging
import pytz
from rest_framework import status
from rest_framework.response import Response
from note.models import Note
from django.contrib.auth.models import User
from services import MailServices
from json import loads

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
    'reminder_test',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id=None,
     consumer_timeout_ms=1000,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))