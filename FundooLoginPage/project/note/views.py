from note.models import Note,Label
from note.serializer import LabelSerializer,UpdateSerializer,SearchSerializer,NoteSerializer,LabelFunctionSerializer,NoteFunctionSerializer
from rest_framework import mixins
from project.settings import file_handler
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
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
obj1=Response()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


@method_decorator(login_required, name='dispatch')
class CreateLabel(generics.GenericAPIView):
   
    serializer_class = LabelSerializer
    queryset= Label.objects.all()

    def get(self, request, *args, **kwargs):
        try:

            user_id = request.user
            label = self.queryset.filter(user_id=user_id)
            return Response(label.values(), status=status.HTTP_200_OK)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)
  
    def post(self,request):
        
        #user_id=request.user_id
        #label = self.queryset.filter(user_id=user_id)
        user_data = LabelSerializer(data=request.data)
        if user_data.is_valid():
            user_data.save()
            return Response({"data": "data created successfully"}, 
                            status=status.HTTP_201_CREATED)
        else:
            error_details = []
            for key in user_data.errors.keys():
                error_details.append({"field": key, "message": user_data.errors[key][0]})

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

@method_decorator(login_required, name='dispatch')
class CreateNote(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset= Label.objects.all()
    def post(self,request):
        note_serializer = NoteSerializer(data=request.data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response({"data": "data created successfully"}, 
                            status=status.HTTP_201_CREATED)
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

@method_decorator(login_required, name='dispatch')
class NoteDetails(generics.ListAPIView):
    
    serializer_class=NoteFunctionSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset= Note.objects.filter(user_id=user)
        print(queryset)
        return queryset
        
        
    
@method_decorator(login_required, name='dispatch') 
class NoteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

# class NoteUpdate(generics.GenericAPIView):
#     serializer_class = NoteSerializer

#     def put(self,request):
#         user = request.user
#         try:
#             instance = Note.objects.get(id=note_id)
#             data = request.data
#             collaborator_list = [] 
#             label = data["label"]
#             data['label'] = [Label.objects.get(name=name, user_id=request.user.id).id for name in label]
#             collaborator = data['collaborators']
#             for email in collaborator:
#                 emails = User.objects.filter(email=email)
#                 user_id = emails.values()[0]['id']
#                 collaborator_list.append(user_id)
#             data['collaborators'] = collaborator_list
#             serializer = UpdateSerializer(instance, data=data, partial=True)
#             if serializer.is_valid():
#                 note_create = serializer.save()
#                 res = obj1.jsonResponse(True, 'note updated', [serializer.data])
#                 if serializer.data['is_archive']:
#                     rdb.set(str(user.id) + "is_archive",
#                                 {note_create.id: str(json.dumps(serializer.data))})
#                     logger.info("note was updated with note id :%s for user :%s ", note_id, user)
#                     return HttpResponse(json.dumps(res, indent=2), status=200)
#                 elif serializer.data['is_bin']:
#                     rdb.set(str(user.id) + "is_bin",
#                                 {note_create.id: str(json.dumps(serializer.data))})
#                     logger.info("note was updated with note id :%s for user :%s ", note_id, user)
#                     return HttpResponse(json.dumps(res, indent=2), status=200)
#                 else:
#                     if serializer.data['reminder']:
#                         rdb.set("reminder",
#                                     {note_create.id: str(json.dumps({"email": user.email, "user": str(user),
#                                                                      "note_id": note_create.id,
#                                                                      "reminder": serializer.data["reminder"]}))})
#                     rdb.set(str(user.id) + "note",
#                                 {note_create.id: str(json.dumps(serializer.data))})
#                     logger.info("note was updated with note id :%s for user :%s ", note_id, user)
#                     return HttpResponse(json.dumps(res, indent=2), status=200)
#             logger.error("note was updated with note id :%s for user :%s ", note_id, user)
#             res = obj1.jsonResponse(False, 'note was not created', '')
#             return HttpResponse(json.dumps(res, indent=2), status=400)
#         except KeyError as e:
#             logger.error("no data was provided from user %s to update", str(e), user)
#             res = obj1.jsonResponse(False, 'note already upto data ', '')
#             return HttpResponse(json.dumps(res, indent=2), status=400)
#         except Exception as e:
#             logger.error("got error :%s for user :%s while updating note id :%s", str(e), user, note_id)
#             res = obj1.jsonResponse(False, 'Something went wrong ', '')
#             return HttpResponse(json.dumps(res, indent=2), status=400)


   
@method_decorator(login_required, name='dispatch')    
class ArchivedNotes(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def get(self,request):
        is_archived=Note.objects.all().filter(is_archived=True, user=request.user)
        print(is_archived)
        serializer_class=NoteSerializer
        return Response(is_archived.values(),status=status.HTTP_200_OK)
        
@method_decorator(login_required, name='dispatch')    
class BinNotes(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def get(self,request):
        is_bin=Note.objects.all().filter(is_bin=True, user=request.user)
        print(is_bin)
        serializer_class=NoteSerializer
        return Response(is_bin.values(),status=status.HTTP_200_OK)

@method_decorator(login_required, name='dispatch')    
class ScheduleReminder(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def get(self,request):
        reminder=Note.objects.all().filter(reminder=False, user_id=request.user)
        print(reminder)
        serializer_class=NoteSerializer
        return Response(reminder.values(),status=status.HTTP_200_OK)
   

class Remider(generics.GenericAPIView):
    def get(self, request):
        try:
            user = request.user
            print(user)
            user_id = user.id
            print(user_id)
            user_note = Note.objects.filter(user_id=user_id)
            print(user_note)
            reminderlist = []
            print(reminderlist)
            completedlist = []
            print(completedlist)
            for i in range(len(user_note.values())):
                if user_note.values()[i]['reminder'] is None:
                    continue
                elif timezone.now() > user_note.values()[i]['reminder']:
                    completedlist.append(user_note.values()[i])
                else:
                    reminderlist.append(user_note.values()[i])
            remid = {
                'reminder': reminderlist,
                'compl': completedlist
            }
            remdstr = str(remid)
            logger.info("Reminders data is loaded for %s", user)
            return HttpResponse(user_note.values(), status=200)
        except Note.DoesNotExist:
            res = obj1.jsonResponse(False, 'Something went wrong ', '')
            logger.info("Reminder unsuccessfull...")
            return HttpResponse(json.dumps(res))


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
        elastic_client = Elasticsearch(hosts=["localhost"])
        
        user_request = SearchSerializer(data=request.data)
        print(user_request)

        if user_request.is_valid():
            query_body = {
                "query": {
                    "bool": {
                        "must": {
                            "match": {  
                                "title": user_request.data.get('title'),
                                #"note": user_request.data.get('note')
                                      
                                }
                            }
                        }
                    }
                }
       
            result = elastic_client.search(index="note", body=query_body)
            print ("total hits:", len(result["hits"]["hits"]))
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
        





