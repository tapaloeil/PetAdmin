from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^animal/$', views.pets, name='pets'),
    url(r'^animal/(?P<pk>\d+)$', views.PetDetailView, name='pet-detail'),
    url(r'^animal/add/$', views.PetCreate, name='PetCreate'),
    url(r'^fa/$', views.fa, name='fa'),
    url(r'^fa/(?P<pk>\d+)$', views.FADetailView, name='fa-detail'),
    url(r'^fa/add/$', views.add_fa, name='add_fa'),    
	url(r'^full/$', views.full, name='full'),
]