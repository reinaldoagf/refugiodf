from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from apps.adoption.views import requestIndex, requestCreate,requestUpdate,requestDelete
urlpatterns = [
	url(r'^/$', requestIndex.as_view(),name='requestIndex'),
    url(r'^/crear$', requestCreate.as_view(
    	success_url=reverse_lazy('request:requestIndex')),name='requestCreate'),
   	url(r'^/editar/(?P<pk>\d+)$', requestUpdate.as_view(
    	success_url=reverse_lazy('request:requestIndex')),name='requestUpdate'),
   	url(r'^/eliminar/(?P<pk>\d+)$', requestDelete.as_view(
    	success_url=reverse_lazy('request:requestIndex')),name='requestDelete'),
]