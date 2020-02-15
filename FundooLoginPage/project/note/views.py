from note.models import Note,Label
from note.serializer import LabelSerializer,SearchNoteSerializer,NoteSerializer,LabelFunctionSerializer,NoteFunctionSerializer
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
from rest_framework import permissions, renderers # new
from note.permissions import IsOwnerOrReadOnly
from elasticsearch import Elasticsearch 
from elasticsearch_dsl import Search, Q 
from project import settings
from project.settings import ELASTICSEARCH_INDEX_NAMES
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
#from note.search import NoteDocument
from django.shortcuts import render
from project import settings
from django.http import HttpResponse
from rest_framework import status
from project.settings import ELASTICSEARCH_INDEX_NAMES
import json
from project.redis_class import Redis
rdb=Redis()
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(login_required, name='dispatch')
class CreateLabel(generics.GenericAPIView,mixins.CreateModelMixin):
    
    serializer_class=LabelSerializer
    def post(self, request, *args, **kwargs):
        return self.create(self.request)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
              
@method_decorator(login_required, name='dispatch')
class LabelDetails(generics.ListAPIView):
    
    serializer_class=LabelSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset= Label.objects.filter(user_id=user)
        return queryset

@method_decorator(login_required, name='dispatch')
class CreateNote(generics.GenericAPIView,mixins.CreateModelMixin):
    
    serializer_class = NoteSerializer
    def post(self, request, *args, **kwargs):
        # cache.set(request.user, Note)
        # print(cache.get(request.user))
        
        return self.create(self.request)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
      
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
        is_archived=Note.objects.all().filter(is_archived=True, user_id=request.user)
        print(is_archived)
        serializer_class=NoteSerializer
        return Response(is_archived.values(),status=status.HTTP_200_OK)
        
@method_decorator(login_required, name='dispatch')    
class BinNotes(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def get(self,request):
        is_bin=Note.objects.all().filter(is_bin=True, user_id=request.user)
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
    



# class SearchNote(generics.GenericAPIView):
#     serializer_class = SearchNoteSerializer
#     queryset = Note.objects.all()
#     print(queryset)
#     # def post(self, request, id=None):
#     #     s=Search.NoteDocument.search().queryset({
#     #         "query": {
#     #             "bool": {
#     #                 "must": [ ]
#     #             }
#     #         },
#     #         "aggs": { }
#     #     })
#     #    s = s.execute()

     