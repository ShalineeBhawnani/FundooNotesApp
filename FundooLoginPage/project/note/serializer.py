from rest_framework import serializers
from .models import Note,Label
from django.contrib.auth.models import User


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
        
        # read_only_fields = ['user']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        # read_only_fields = ['user']
