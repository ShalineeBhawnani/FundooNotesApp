from note.models import Note,Label
from note.serializer import LabelSerializer,ArchiveNoteSerializer,RestoreNoteSerializer,Userserializer,ReminderSerializer,UpdateSerializer,SearchSerializer,NoteSerializer,LabelFunctionSerializer,NoteFunctionSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.conf import settings
from rest_framework import permissions, renderers 
from note.permissions import IsOwnerOrReadOnly
from elasticsearch import Elasticsearch 
from project import settings
from django.http import JsonResponse
from note.search import NoteDocument
from django.shortcuts import render
from project import settings
from django.http import HttpResponse
from rest_framework import status
import json
import logging
from datetime import timedelta
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import HttpResponse, Http404, HttpResponseNotAllowed
from project.redis_class import Redis
rdb=Redis()
import pytz
import datetime
import logging
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
obj1=Response()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
from rest_framework.decorators import api_view
from utils import smd_response,Smd_Response
from .service.note import NoteService,label_update_in_redis,update_redis
# import pickle
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
import jwt
from django.core.mail import send_mail
from project.settings import SECRET_KEY
from project import decorators   
from project.settings import EMAIL_HOST_USER
from project.CollabratorService import CollaboratorService 
# @method_decorator(login_required(login_url='/login/'))
class CreateLabel(generics.GenericAPIView):
    
    serializer_class = LabelSerializer
    queryset= Label.objects.all()
    
    def get(self, request, *args, **kwargs):
        token = request.headers.get('Token')
        mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id=mytoken.get('username') 
        user=User.objects.get(username=user_id)
        try:
            label = self.queryset.filter(user_id=user.id)
            return Response(label.values(), status=status.HTTP_200_OK)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)
        
   
    def post(self,request,id=None):
        # pdb.set_trace()
        print("post request")
        # user_id=request.user
        # print(user_id)
        # label = self.queryset.filter(user_id=user_id)
        print(request.data)
        
        serializer = LabelSerializer(data=request.data)
        print(request.data)
        print(serializer) #TODO Token Auth decorator
        if serializer.is_valid():
            token = request.headers.get('Token')
            mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id=mytoken.get('username')
            user=User.objects.get(username=user_id)
            serializer.save(user_id=user.id)
            return Response("label added")
            # return Response({"data": "data created successfully"}, 
            #                 status=status.HTTP_201_CREATED)
        else:
            error_details = []
            for key in serializer.errors.keys():
                error_details.append({"field": key, "message": serializer.errors[key][0]})

            data = {
                    "Error": {
                        "status": 400,
                        "message": "some error is there please check..",
                        "error": error_details
                        }
                    }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)
  
              
@method_decorator(login_required, name='dispatch')
class LabelDetails(generics.ListAPIView):
    
    serializer_class=LabelSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset= Label.objects.filter(user_id=user)
        return queryset
        
class CreateNote(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset= Note.objects.all().filter(is_archived=False,is_bin=False,reminder__isnull=True)
    def get(self, request, *args, **kwargs):
        token = request.headers.get('Token')
        mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id=mytoken.get('username')
        user=User.objects.get(username=user_id)
        # user=request.user
        try:
            # data = request.data
            # username = data.get('username')
            # print(username)
            # user_id = request.user
            # print(user_id)
            note = self.queryset.filter(user_id=user.id)
            # return Response(note.values(), status=status.HTTP_200_OK)
            return Response(note.values())
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)
    
    def post(self,request):
        data=request.data
        note_serializer = NoteSerializer(data=request.data)
        print(note_serializer)
        if note_serializer.is_valid():
            token = request.headers.get('Token')
            mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id=mytoken.get('username')
            user=User.objects.get(username=user_id)
            #user=request.user
            mycollb = request.data.get('collaborators')
            # collab =data['collaborators']
            print("mycollb",mycollb)
            collaborators_list = []
            print("list collab",collaborators_list)
            for email in mycollb:
                print("email",mycollb)
                user = User.objects.get(id=mycollb)
                email=user.email
                print(email)
                collaborators_list.append(user.id)
                print("append",collaborators_list)
            data=request.data    
            print(data)
            # data._mutable = True
            data['collaborators'] = collaborators_list
            # data._mutable = False
            print("final ",data['collaborators'] )
            print("list collaborators",collaborators_list)
            note_serializer = NoteSerializer(data=request.data)
            if note_serializer.is_valid():
                note_serializer.save(user_id=user.id)
              # note_serializer.save(user_id=user.id)
          
            return Response("Note added")
            # return Response({"data": "Note added"}, 
            #                 status=status.HTTP_201_CREATED)
        else:
            error_details = []
            for key in note_serializer.errors.keys():
                error_details.append({"field": key, "message": note_serializer.errors[key][0]})

            data = {
                    "Error": {
                        "status": 400,
                        "message": "Your submitted data was not valid - please correct the below errors",
                        "error_details": error_details
                        }
                    }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)

# @method_decorator(login_required, name='dispatch')
class NoteDetails(generics.ListAPIView):
    
    serializer_class=NoteFunctionSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset= Note.objects.filter(user_id=user)
        print(queryset)
        return queryset
        
class NoteUpdate(generics.GenericAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

    def put(self,request,pk):
        token = request.headers.get('Token')
        mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id=mytoken.get('username')
        user=User.objects.get(username=user_id)
        note = Note.objects.get(id=pk,user_id=user.id)
        serializer = NoteSerializer(note,data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user.id)
            return Response("Note Edited")
  
# class ArchivedNotes(generics.GenericAPIView):
    
#     def get(self, request, *args, **kwargs):
#         print("get request")
#         token = request.headers.get('Token')
#         print(token)
#         mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         print(SECRET_KEY)
#         print(mytoken)
#         print(str(mytoken))
#         user_id=mytoken.get('username')
#         print(user_id)
#         user=User.objects.get(username=user_id)
#         print(user)
#         is_archived=Note.objects.all().filter(is_archived=True,user_id=user.id)
#         print(is_archived)
#         serializer_class=NoteSerializer
#         return Response(is_archived.values(),status=status.HTTP_200_OK)
        
 
class ArchivedNotes(generics.GenericAPIView):
    serializer_class = ArchiveNoteSerializer
    queryset = Note.objects.all()
   
    def get(self, request):
        token = request.headers.get('Token')
        mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id=mytoken.get('username')
        user=User.objects.get(username=user_id)
        note = Note.objects.filter(is_archived=True, user_id=user.id)
        seri = NoteSerializer(note, many=True)
        return Response(seri.data, status=status.HTTP_200_OK)

class BinNotes(generics.GenericAPIView):
    serializer_class = RestoreNoteSerializer
    queryset = Note.objects.all()

    def get(self,request):
        try:
            token = request.headers.get('Token')
            print(token)
            received_token = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
            token_username = received_token.get('username')
            user=User.objects.get(username=token_username)
            userid = User.objects.get(id=user.id)
            note = Note.objects.filter(is_bin=True , user_id=userid)
            serial_class = NoteSerializer(note, many=True)
            return Response(serial_class.data)
        except Note.DoesNotExist:
            return Response("Not found")

# @method_decorator(login_required, name='dispatch')   
class Remider(generics.GenericAPIView):
    def get(self, request, id=None):
       
        try:
            token = request.headers.get('Token')
            mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id=mytoken.get('username')
            user=User.objects.get(username=user_id)
            notes_with_reminder = Note.objects.filter(user_id=user.id, reminder__isnull=False)
            return Response(notes_with_reminder.values(), status=status.HTTP_200_OK)
        except Exception:
            smd = {'success': 'Fail', 'message': 'something wrong in reminder', 'data': []}
            return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        
class ReminderUpdate(generics.GenericAPIView):
    serializer_class= ReminderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def put(self,request,id):
        user = request.user
        notes_with_reminder = list(Note.objects.filter(user_id=user,reminder__isnull=False))
        print(notes_with_reminder)
        timezone = pytz.timezone("UTC")
        if len(notes_with_reminder) > 0:
            print(len(notes_with_reminder))
            for note in list(notes_with_reminder):
                t = type(note.reminder)
                if t is None or note.reminder == '':
                    break
                reminder_time = note.reminder
                reminder_time_byte = str.encode(str(reminder_time))
                note_id = str.encode(str(note.id))
                #email.send('note_reminder', reminder_time_byte, note_id) 
                print(note_id)
                return Response(reminder_time_byte, status=status.HTTP_200_OK)
     
  

@method_decorator(login_required, name='dispatch') 
class LabelUpdate(generics.GenericAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    lookup_field='id'

    serializer_class=LabelFunctionSerializer
    queryset = Label.objects.all()
    def put(self,request,id):
        user = self.request.user
        print("user:",user)
        user_id= self.request.user.id
        print(user_id)

        print(user)
        return self.update(request,id=user_id)
    
    def delete(self,request,id=None):
        user = self.request.user
        user_id= self.request.user.id
        return self.destroy(request,user_id)

@method_decorator(login_required, name='dispatch') 
class SearchNote(generics.GenericAPIView):
    serializer_class = SearchSerializer
    queryset = Note.objects.all()
    
    def post(self, request, id=None):
        # elastic_client = Elasticsearch(hosts=["localhost"])
        user_request = SearchSerializer(data=request.data)
        print(user_request)
        if user_request.is_valid():
            user=request.user
            print(user)
            search_result = NoteDocument().search().query({
                'bool': {
                    'must': [
                        {'match': {'title': user_request.data.get('title')}},
                        {'match': {'note': user_request.data.get('note')}},   
                    ]
                },
               
            })
            
            result = search_result.execute()
            print(result)
            note_search = [Note.objects.filter(user_id=user.id, title=hits.title, note=hits.note).values()
                         for hits in result.hits]

            return Response(note_search, status=status.HTTP_200_OK)
        else:
            return Response("not found", status=status.HTTP_400_BAD_REQUEST)


    

       

           
           




# class NoteUpdate(generics.GenericAPIView):

#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     def get(self, request, pk):
#         try:
#             note = Note.objects.get(id=pk, user_id=self.request.user.id)
#             coll = note.collaborators.filter(id=pk)
#             print(coll)
#             print(Note.objects.filter(user_id=request.user.id).count())
#             if (Note.objects.filter(user_id=request.user.id).count() > 0 or
#                 note.collaborators.filter(id=request.user.id).count() == 1):
#                 serializer = NoteSerializer(note)
#                 return Response(serializer.data)
#             else:
#                 serializer = NoteSerializer(note)
#                 return Response(serializer.data)

#         except Note.DoesNotExist:
#             return Response("this note does not exit", status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk):
#         try:
#             note = Note.objects.get(id=pk, user_id=self.request.user.id)
#             serializer = NoteSerializer(note, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#             from_email = self.request.user.email
#             coll = note.collaborators.all()
#             collaborator = []
#             for user_name in coll:
#                 u = user_name.email
#                 collaborator.append(u)
#             print("cool : ",collaborator)
#             if collaborator == []:
#                 print("No collaborator list")

#             else:
#                 send_mail('Note id {}'.format(note.id),'sharing note',EMAIL_HOST_USER,collaborator)
#                 print("send_mail",EMAIL_HOST_USER)
#             return Response('Note updated', status=status.HTTP_202_ACCEPTED)
#         except Note.DoesNotExist:
#             return Response("this note does not exit", status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk):
#         try:
#             note = Note.objects.get(id=pk)
#             print(note)
#             note.delete()

#             return Response("Note deleted", status=status.HTTP_202_ACCEPTED)

#         except Notes.DoesNotExist:
#             return Response("Not found", status=status.HTTP_404_NOT_FOUND)


# class UpdateNoteList(GenericAPIView):

#     serializer_class = DisplayNoteSerializer
#     def get(self,request,pk):

#         user = User.objects.get(id=self.request.user.id)
#         note = Notes.objects.get(id=pk,user_id=user.id)
#         serial_class = DisplayNoteSerializer(note)
#         return Response(serial_class.data)

#     def put(self,request,pk):
#         token = request.headers.get('Token')
#         print(token)
#         received_token = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
#         token_username = received_token.get('username')
#         user=User.objects.get(username=token_username)
#         print(user)
#         note = Notes.objects.get(id=pk,user_id=user.id)
#         serializer = CreateNoteSerializer(note,data=request.data)
#         if serializer.is_valid():
#             serializer.save(user_id=user.id)
#             return Response("Notes Updated Successfully")
#         return Response('Oops Something went Wrong')


# class ArchiveNoteList(GenericAPIView):

#     serializer_class = DisplayNoteSerializer
#     queryset = Notes.objects.all()

#     def get(self,request):
#         user = User.objects.get(id=self.request.user.id)
#         note = Notes.objects.filter(archive = True,user_id=user.id)
#         serial_class = DisplayNoteSerializer(note,many=True)
#         return Response(serial_class.data)   

# class PinNoteList(GenericAPIView):

#     serializer_class = DisplayNoteSerializer
#     queryset = Notes.objects.all()

#     def get(self,request):
#         user = User.objects.get(id=self.request.user.id)
#         note = Notes.objects.filter(pin = True,user_id=user.id)
#         serial_class = DisplayNoteSerializer(note,many=True)
#         return Response(serial_class.data)


# class TrashNote(GenericAPIView):

#     serializer_class = RestoreNoteSerializer
#     queryset = Notes.objects.all()

#     def get(self,request,pk):
#         try:
#             user = User.objects.get(id=self.request.user.id)
#             note = Notes.objects.get(id = pk ,trash=True, user_id=user)
#             serial_class = DisplayNoteSerializer(note)
#             return Response(serial_class.data)
#         except Notes.DoesNotExist:
#             return Response("Not found")

#     def put(self,request,pk):
#         user = User.objects.get(id=self.request.user.id)
#         note = Notes.objects.get(id=pk,user_id=self.request.user.id)
#         serializer = RestoreNoteSerializer(note,data=request.data)
#         if serializer.is_valid():
#             serializer.save(user_id=self.request.user.id)
#             return Response('Restore Note')

