from django.conf import settings
from elasticsearch import helpers,Elasticsearch
from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)
from elasticsearch_dsl import analyzer
from project import settings
#from project.settings import ELASTICSEARCH_INDEX_NAMES
from .models import Note,Label
from django_elasticsearch_dsl.registries import registry


#Document index
# Name of the Elasticsearch index
note = Index('note')
print(note)

# See Elasticsearch Indices API reference for available settings
note.settings(
    number_of_shards=1,
    number_of_replicas=0
)
#analyzer is basically the combination of three lower level blocks Character Filters, Tokenizers & Token Filters
html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

#hold all the required information
@registry.register_document
class NoteDocument(Document):
    user = fields.ObjectField(properties= {
        'username' : fields.TextField(),
        'email' : fields.TextField(),
        'password' : fields.TextField()
       
    })  
    #print(user)
    label_note = fields.NestedField(properties={
        'label': fields.TextField(analyzer=html_strip),
        'user_id' : fields.TextField(analyzer=html_strip),
      })
    
    class Django(object):
        
        model = Note # The model associate with this Document
        #related_models = [Label]
        fields = [
            'title',
            'color',
            'note',
            'reminder',
        ]
        
    class Index:
        name = 'note'

    
    # def get_instances_from_related(self, related_instance):
    #     if isinstance(related_instance, Label):
    #         return related_instance.label

    #     # otherwise it's a Manufacturer or a Category
    #     return related_instance.label_note_set.all()
 