from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^animal/$', views.pets, name='pets'),
    url(r'^animal/add/$', views.add_pet, name='add_pet'),
    url(r'^fa/$', views.fa, name='fa'),
    url(r'^fa/add/$', views.add_fa, name='add_fa'),    
	url(r'^full/$', views.full, name='full'),
]