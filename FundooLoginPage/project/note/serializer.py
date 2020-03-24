from rest_framework import serializers
from .models import Note,Label
from django.contrib.auth.models import User
#from .search import NoteDocument
import json

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['label']
        # fields = '__all__'
class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'mail']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note

        # fields = '__all__'
        fields = ['title','note', 'label_note','add_picture', 'is_archived', 'is_bin', 'color',
                  'is_pinned', 'more', 'reminder', 'collaborators','created_on','last_edited']
        # fields=['title','note']
      
        #read_only_fields = ['user']

class SearchSerializer(serializers.ModelSerializer):
    class Meta:

        model = Note
        fields = ['title', 'reminder', 'color', 'note']

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['user','email']
        
class NoteFunctionSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Note
        fields = ['title', 'label_note','add_picture', 'is_archived', 'is_bin', 'color',
                  'is_pinned', 'more', 'reminder', 'collaborators']

class LabelFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['label']

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'note', 'label', 'url','collaborators']
        
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['reminder']
# label_note = LabelSerializer(many=True, read_only=True)
#         collaborators = CollaboratorSerializer(many=True, read_only=True)



class RestoreNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['is_bin']

class ArchiveNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['is_archived']