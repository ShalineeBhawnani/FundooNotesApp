from kafka import KafkaProducer,KafkaConsumer
from json import loads,dumps
import datetime
import logging
import pytz
from rest_framework import status
from rest_framework.response import Response
from note.models import Note
from django.contrib.auth.models import User
from services import MailServices
from json import loads
import json
import logging
LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

KAFKA_PRODUCER = None
def get_kafka_producer():
    KAFKA_PRODUCER = init_kafka_producer_instance()
    return KAFKA_PRODUCER

def init_kafka_producer_instance():
    try:

        if KAFKA_PRODUCER is not None :
            return KAFKA_PRODUCER

        producer = None
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
        return producer
    except Exception as e:
        import traceback
        print(traceback.format_exc())
    return None


KAFKA_CONSUMER = None
def get_kafka_consumer():
    KAFKA_CONSUMER = init_kafka_consumer_instance()
    return KAFKA_PRODUCER

def init_kafka_consumer_instance():
    try:

        if KAFKA_CONSUMER is not None :
            return KAFKA_CONSUMER

        consumer = None
        consumer = KafkaConsumer('reminder_test',
                    bootstrap_servers=['localhost:9092'],
                    auto_offset_reset='earliest',
                    enable_auto_commit=True,
                    group_id=None,
                    consumer_timeout_ms=1000,
                    value_deserializer=lambda x: loads(x.decode('utf-8')))
        return consumer
    except Exception as e:
        import traceback
        print(traceback.format_exc())
    return None

def send_message(self):
    user_reminder = list(Note.objects.filter(reminder__isnull=False))
    timezone = pytz.timezone("UTC")

    if len(user_reminder) > 0:
            for note in list(user_reminder):
                t = type(note.reminder)
                #logging.debug('This message should go to the log file')
                logging.info('TYPE OF REMINDER -------------->>>> {t}')
                if t is None or note.reminder == '':
                    break
                reminder_time = note.reminder
                reminder_time_byte = str.encode(str(reminder_time))
                note_id = str.encode(str(note.id))
                
    logging.info('Message Posted To Kafka Topic')

    # try:
    #     if topic is None or reminder_test is None:
    #         raise Exception("Invalid argument topic or data")
    #     producer = get_kafka_producer()
    #     if producer is not None:
    #         x = producer.send('reminder_test', reminder_test,note_id)
    #         print(x)
    # except Exception as e:
    #     import traceback
    #     print(traceback.format_exc())
        
 


# def delete_topic(topic):
#     try:
#         if topic is None:
#             raise Exception("Topic is None")
#     except Exception as e:
#         import traceback
#         print(traceback.format_exc())


# def create_kafka_topic_name(obj) :
#     try :
#         if offering is None :
#             raise Exception("Invalid argument offering, unable to create topic name")
#         return str(obj.order_id)
#     except Exception as e :
#         print(e)
#     return None