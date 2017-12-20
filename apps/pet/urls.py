from django.conf.urls import url
from apps.pet.views import indexPet, createPet
urlpatterns = [		
    url(r'^$', indexPet,name='pet_index'),
    url(r'^crear$', createPet,name='pet_create'),
]