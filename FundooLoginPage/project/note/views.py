from django.shortcuts import render
from note.models import Label,Note
from note.serializer import LabelSerializer, NoteSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import mixins
#from .permissions import IsOwner
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

@method_decorator(login_required(login_url='login/'),name='dispatch')
class NoteListCreate(generics.CreateAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    #permission_classes = [IsAuthenticated]

@method_decorator(login_required(login_url='login/'),name='dispatch')
class LabelList(generics.CreateAPIView):

    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class NoteListDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteListDetail(generics.RetrieveAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteListUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer