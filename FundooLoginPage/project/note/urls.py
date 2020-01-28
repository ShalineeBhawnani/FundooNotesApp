from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^', include('note.urls')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/', include(router.urls)),
    url(r'^$', views.index, name='index'),
     #path('index/',index, name='index')
]