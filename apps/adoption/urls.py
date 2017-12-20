from django.conf.urls import url
from apps.adoption.views import indexRequest, createRequest
urlpatterns = [
	url(r'', indexRequest,name='request_index'),
    url(r'craer/', createRequest,name='request_create'),
]