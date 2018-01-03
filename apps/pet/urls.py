from django.conf.urls import url

from django.contrib.auth.decorators import login_required
from apps.pet.views import petIndex, petCreate, petUpdate, petDelete, listView
urlpatterns = [	
    url(r'^/crear$', login_required(petCreate),name='petCreate'),	
    url(r'^/editar/(?P<id>\d+)$', login_required(petUpdate),name='petUpdate'),
    url(r'^/eliminar/(?P<id>\d+)$', login_required(petDelete),name='petDelete'),
    url(r'^/', login_required(petIndex),name='petIndex'),
    url(r'/listado',listView,name='list')
]