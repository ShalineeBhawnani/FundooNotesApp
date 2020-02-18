from note.models import Note,Label
from note.serializer import LabelSerializer,SearchSerializer,NoteSerializer,LabelFunctionSerializer,NoteFunctionSerializer
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
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import HttpResponse, Http404, HttpResponseNotAllowed
from project.redis_class import Redis
rdb=Redis()
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


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
        reminder=Note.objects.all().filter(is_bin=True, user_id=request.user)
        print(reminder)
        serializer_class=NoteSerializer
        return Response(reminder.values(),status=status.HTTP_200_OK)
   
    
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
        





