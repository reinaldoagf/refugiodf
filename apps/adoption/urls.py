from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from apps.adoption.views import requestIndex, requestCreate
urlpatterns = [
	url(r'^/$', requestIndex.as_view(),name='requestIndex'),
    url(r'^/crear$', requestCreate.as_view(success_url=reverse_lazy('request:requestIndex')),name='requestCreate'),
]