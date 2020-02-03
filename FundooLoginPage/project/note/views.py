from django.shortcuts import render
from note.models import Label,Note
from note.serializer import LabelSerializer, NoteSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import permissions

class NoteListCreate(generics.CreateAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LabelList(generics.CreateAPIView):

    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class NoteListDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteListDetail(generics.RetrieveAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteListUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer