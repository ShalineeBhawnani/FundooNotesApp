from note.models import Note,Label
from note.serializer import LabelSerializer,NoteSerializer,SearchNoteSerializer,NoteFunctionSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response


class CreateLabel(generics.GenericAPIView,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class=LabelSerializer
    queryset =  Label.objects.all()
    lookup_field='id'
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
            
    def post(self, request, *args, **kwargs):
        return self.create(self.request)
    
    def perform_create(self,serializer):
        serializer.save(user_id=self.request.user)
        

    def put(self,request,id=None):
        print("editated")
        return self.update(request,id)
        
    
    def delete(self,request,id=None):
        return self.destroy(request,id)
        
        
        