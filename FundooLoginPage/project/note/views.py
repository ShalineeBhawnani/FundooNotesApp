from django.shortcuts import render
from note.models import Label,Note
from note.serializer import LabelSerializer, NoteSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import permissions,authentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
import datetime
import json
import django
import jwt
from snippets.token import token_activation,token_validation,account_activation_token
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from note.decorators import login_decorator
#from rest_framework import permissions
#from note.permissions import IsOwnerOrReadOnly
#from rest_framework.authentication import TokenAuthentication

@method_decorator(login_required(login_url='/login/'),name='dispatch')
#@method_decorator(login_decorator,name='dispatch')
class NoteListCreate(generics.CreateAPIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # def perform_create(self,serializer):
    #     serializer. save(user=self.request.user)


#@method_decorator(login_required(login_url='login/'),name='dispatch')
#@method_decorator(label_decorator,name='dispatch')
class LabelListCreate(generics.CreateAPIView):
    #authentication_classes = [TokenAuthentication]
    print("authenticate")
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                        IsOwnerOrReadOnly]

    serializer_class = LabelSerializer
    queryset = Label.objects.all()
#@method_decorator(label_decorator,name='dispatch')
class NoteListDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
#@method_decorator(label_decorator,name='dispatch')
class NoteListDetail(generics.RetrieveAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                        IsOwnerOrReadOnly]
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

#@method_decorator(label_decorator,name='dispatch') 
class NoteListUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    