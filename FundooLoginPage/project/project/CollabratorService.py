from note.models import Note
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class CollaboratorService:

    @staticmethod
    def get_collaborators(serializer):
        collaborators_input = serializer.data.get('collaborators')  # collaborator input has list of emails
        list_of_collaborators = []
        for collaborator_pk in collaborators_input:
            user = User.objects.get(pk=collaborator_pk)
            list_of_collaborators.append(user.id)
        return list_of_collaborators
