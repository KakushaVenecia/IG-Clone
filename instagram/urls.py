from django.urls import re_path as url 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url(r'^$', views.landing, name='landing'),
    url(r'^register$', views.register, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^post$', views.post, name='post'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^search/', views.search_results, name='search_results'),
    url('profile/', views.profile, name='profile'),
    url('user_profile/<username>/', views.user_profile, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)