from django.core.exceptions import PermissionDenied
from note.models import Label,Note

def label_decorator(function):

    def wrap(request, *args, **kwargs):
        label = label.objects.get(pk=kwargs['user_id'])
        if entry.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

