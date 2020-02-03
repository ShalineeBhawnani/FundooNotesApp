from django.shortcuts import render
from note.models import Label,Note
from note.serializer import LabelSerializer, NoteSerializer
from rest_framework import generics


class NoteList(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class LabelList(generics.CreateAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
