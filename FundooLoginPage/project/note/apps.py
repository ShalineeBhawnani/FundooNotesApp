from django.apps import AppConfig


class NoteConfig(AppConfig):
    name = 'note'
    
    # def ready(self):
    #     from note import schedule
    #     schedule.start()