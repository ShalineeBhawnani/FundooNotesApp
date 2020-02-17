from rest_framework import serializers
from .models import Note,Label
from django.contrib.auth.models import User
#from .search import NoteDocument
import json

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
        #read_only_fields = ['user']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['user']

class SearchSerializer(serializers.ModelSerializer):
    class Meta:

        model = Note
        fields = ['title', 'reminder', 'color', 'label_note']


class NoteFunctionSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Note
        fields = ['title', 'label_note','add_picture', 'is_archived', 'is_bin', 'color',
                  'is_pinned', 'more', 'reminder', 'collaborators']

class LabelFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['label']
        