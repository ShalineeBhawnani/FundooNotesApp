from note.models import Note,Label
from note.serializer import LabelSerializer,NoteSerializer,LabelFunctionSerializer,NoteFunctionSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



@method_decorator(login_required, name='dispatch')
class CreateLabel(generics.GenericAPIView,mixins.CreateModelMixin):
    
    serializer_class=LabelSerializer
    def post(self, request, *args, **kwargs):
        return self.create(self.request)
    
    def perform_create(self,serializer):
        serializer.save(user_id=self.request.user)
              
@method_decorator(login_required, name='dispatch')
class LabelDetails(generics.ListAPIView):
    
    serializer_class=LabelSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset= Label.objects.filter(user_id=user)
        return queryset

@method_decorator(login_required, name='dispatch')
class CreateNote(generics.GenericAPIView,mixins.CreateModelMixin):
    
    serializer_class=NoteSerializer
    def post(self, request, *args, **kwargs):
        # cache.set(request.user, Note)
        # print(cache.get(request.user))
        
        return self.create(self.request)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
      
@method_decorator(login_required, name='dispatch')
class NoteDetails(generics.ListAPIView):
    
    serializer_class=NoteFunctionSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset= Note.objects.filter(user_id=user)
        print(queryset)
        return queryset
        
        
    
@method_decorator(login_required, name='dispatch') 
class NoteUpdate(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='id'

    serializer_class=NoteSerializer
    queryset= Note.objects.all()


    def put(self,request,id):
       
        user = self.request.user
        user_id= self.request.user
        user= Note.objects.filter(id=id)

        print(user)
        return self.update(request,id=id)

    def delete(self,request,id=None):
        user = self.request.user
        # user=user.objects.get(id)
        id= self.request.user
        return self.destroy(request,id)


            
    
@method_decorator(login_required, name='dispatch') 
class LabelUpdate(generics.GenericAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    lookup_field='id'

    serializer_class=LabelFunctionSerializer
    queryset = Label.objects.all()
    def put(self,request,id):
        user = self.request.user
        print("user:",user)
        user_id= self.request.user.id
        print(user_id)

        print(user)
        return self.update(request,id=user_id)
    
    def delete(self,request,id=None):
        user = self.request.user
        user_id= self.request.user.id
        return self.destroy(request,user_id)
        

    