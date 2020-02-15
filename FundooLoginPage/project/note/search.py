#from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
#from project import settings
#from project.settings import ELASTICSEARCH_INDEX_NAMES
from .models import Note,Label
from django_elasticsearch_dsl.registries import registry


#Document index
# Name of the Elasticsearch index
#INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])
#print(INDEX)
note = Index('note')

# See Elasticsearch Indices API reference for available settings
note.settings(
    number_of_shards=1,
    number_of_replicas=0
)
#analyzer is basically the combination of three lower level blocks Character Filters, Tokenizers & Token Filters
html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@registry.register_document
#@note.doc_type
class NoteDocument(Document):
    label_note = fields.ObjectField(properties={
        
        'label': fields.TextField(analyzer=html_strip),
        'user': fields.TextField(analyzer=html_strip)
         
        
    })
    print(label_note)
    # user = fields.ObjectField(properties= {
    #     'username' : fields.TextField(),
    #     'email' : fields.TextField(),
    #     'password' : fields.TextField()
    # })
    
    print("hi I am label note", label_note)
    class Django(object):
    # class Meta:
        """Inner nested class Django."""
        # we removed the type field from here
        model = Note # The model associate with this Document
        # related_models = [Label]
        # fields = [
        #     'title',
        #     'color',
        #     'reminder'
        # ]
        
    # def get_instances_from_related(self, label_note):
    #     return label_note.all()