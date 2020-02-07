from rest_framework import serializers
from .models import Note,Label
from django.contrib.auth.models import User

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
        # fields = [
        #     "id",
        #     "user_id",
        #     "label"
        # ]
        
        # read_only_fields = ['user']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        # read_only_fields = ['user']

class SearchNoteSerializer(serializers.ModelSerializer):
    class Meta:

        model = Note
        fields = ['title', 'note', 'reminder', 'color', 'label']

class NoteFunctionSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Note
        fields = ['title', 'note', 'note_image', 'labels', 'collaborators', 'is_archived', 'is_trashed', 'color',
                  'is_pinned', 'link', 'reminder']