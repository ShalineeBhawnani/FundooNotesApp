import logging
import pickle

from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.utils import timezone
from project.redis_class import Redis
rdb=Redis()
from note.models import Label
from note.models import Note
from note.serializer import NoteSerializer
from utils import smd_response

logger = logging.getLogger(__name__)
User = get_user_model()

class NoteService:

    def reminder_notes(self, user):
    
        try:
            fired_reminder = rdb.get(str(user.username) + 'fired_reminders')
            upcoming_reminder = rdb.get(user.username + 'upcoming_reminders')
            print(user)
            if fired_reminder or upcoming_reminder:
                print("ok")
                note = pickle.loads(fired_reminder)
                print(note)
                notes_upcoming = pickle.loads(upcoming_reminder)
                print(notes_upcoming)

                fired_reminder_serializer = NoteSerializer(note, many=True)
                print(fired_reminder_serializer)
                upcoming_reminder_serializer = NoteSerializer(notes_upcoming, many=True)
                print(upcoming_reminder_serializer)

                smd = smd_response(True, 'successfully', data={'fired': fired_reminder_serializer.data,
                                                               'upcoming': upcoming_reminder_serializer.data})
                logger.info('successfully get notes from redis')
                return smd
            fired_reminder_object = Note.objects.filter(user_id=int(user.id), reminder__lte=timezone.now())
            upcoming_reminder_object = Note.objects.filter(user_id=user.id, reminder__gte=timezone.now())
            if fired_reminder_object or upcoming_reminder_object:
                fired_serializer = NoteSerializer(upcoming_reminder_object, many=True)
                upcoming_serializer = NoteSerializer(fired_reminder_object, many=True)

                fired_reminder_notes = pickle.dumps(fired_reminder_object)
                upcoming_reminder_notes = pickle.dumps(upcoming_reminder_object)

                rdb.set(str(user.username) + 'fired_reminders', fired_reminder_notes)
                rdb.set(user.username + 'upcoming_reminders', upcoming_reminder_notes)

                smd = smd_response(True, 'successfully',
                                   data={'fired': fired_serializer.data, 'upcoming': upcoming_serializer.data})
                logger.info('successfully get notes from database')
            else:
                smd = smd_response(False, 'for this user reminder not exists')
        except Note.DoesNotExist:
            smd = smd_response(False, 'please enter valid user for get a note')
            logger.error('note not exist for this note id error from Note.views')
        except ValueError:
            smd = smd_response(False, 'please enter user_id in digits')
        except Exception:
            logger.error('exception occurred while getting all notes error from Note.views')
            smd = smd_response()
        return smd