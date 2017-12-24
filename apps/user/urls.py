from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from apps.user.views import userCreate
from django.contrib.auth.views import login
urlpatterns = [	
    # url(r'^/$', userIndex.as_view(),name='userIndex'),
    url(r'^/crear$', userCreate.as_view(
    	success_url=reverse_lazy('indexPage')),name='userCreate'),
    url(r'^/login$', login,{'template_name':'userLogin.html'},name='userLogin'),
   	# url(r'^/editar/(?P<pk>\d+)$', userUpdate.as_view(
    # 	success_url=reverse_lazy('user:userIndex')),name='userUpdate'),
   	# url(r'^/eliminar/(?P<pk>\d+)$', userDelete.as_view(
    # 	success_url=reverse_lazy('user:userIndex')),name='userDelete'),
]