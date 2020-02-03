from django.urls import path
from django.conf.urls import url, include
from note import views
from note.views import NoteList,LabelList

urlpatterns = [
    path('note/', views.NoteList.as_view() ,name="note"),
    path('label/', views.LabelList.as_view() ,name="label"),
]
