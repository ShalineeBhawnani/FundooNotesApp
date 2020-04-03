from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Registration,Profile

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'password2': {
                'write_only': True
            }
        }

class AllUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username', 'email']
        

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
        'password': {
            'write_only': True
        }
    }


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        fields = ['email']

class ResetPasswordSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password','password2']
        
        

class UserUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']
        