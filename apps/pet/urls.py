from django.conf.urls import url
from apps.pet.views import petIndex, petCreate, petUpdate, petDelete
urlpatterns = [	
    url(r'^crear', petCreate,name='petCreate'),	
    url(r'^editar/(?P<id>\d+)', petUpdate,name='petUpdate'),
    url(r'^eliminar/(?P<id>\d+)', petDelete,name='petDelete'),
    url(r'^', petIndex,name='petIndex'),
]