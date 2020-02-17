from django.urls import path
from django.conf.urls import url, include
from note import views
from note.views import LabelDetails,ArchivedNotes,SearchNote,ScheduleReminder,NoteDetails,BinNotes,CreateLabel,CreateNote,NoteUpdate,LabelUpdate
# LabelListCreate,NoteListDetail,NoteListDelete,NoteListUpdate
from django.contrib.auth.decorators import login_required, permission_required



urlpatterns = [
    path('note/', views.CreateNote.as_view() ,name="note"),
    path('label/', views.CreateLabel.as_view() ,name="label"),
    path('labeldetails/',views.LabelDetails.as_view(), name= "labeldetails"),
    path('notedetails/', views.NoteDetails.as_view() ,name="notedetails"),
    path('noteupdate/', views.NoteUpdate.as_view() ,name="noteupdate"),
    path('noteupdate/<int:pk>/', views.NoteUpdate.as_view() ,name="noteupdate"),
    path('labelupdate/<int:id>/', views.LabelUpdate.as_view() ,name="noteupdate"),
    path('search/', SearchNote.as_view(),name="search"),
    path('archive/', ArchivedNotes.as_view(),name="archive"),
    path('bin/', BinNotes.as_view(),name="bin"),
    path('reminder/', ScheduleReminder.as_view(),name="reminder")

    


]

