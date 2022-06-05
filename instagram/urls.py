from django.urls import re_path as url 
from . import views

urlpatterns =[
    url(r'^$', views.landing, name='landing'),
    url(r'^timeline$', views.timeline, name='timeline'),
    url(r'^register$', views.register, name='signup'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^logout$', views.logout, name='logout'),
]