from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from apps.adoption.views import requestIndex, requestCreate,requestUpdate,requestDelete
urlpatterns = [
	url(r'^/$', login_required(requestIndex.as_view()),name='requestIndex'),
    url(r'^/crear$', login_required(requestCreate.as_view(
    	success_url=reverse_lazy('request:requestIndex'))),name='requestCreate'),
   	url(r'^/editar/(?P<pk>\d+)$', login_required(requestUpdate.as_view(
    	success_url=reverse_lazy('request:requestIndex'))),name='requestUpdate'),
   	url(r'^/eliminar/(?P<pk>\d+)$', login_required(requestDelete.as_view(
    	success_url=reverse_lazy('request:requestIndex'))),name='requestDelete'),
]