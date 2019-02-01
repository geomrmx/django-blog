from django.urls import path
from django.conf.urls import url
from blog import views

urlpatterns = [    
    path('', views.post_list, name="post_list"),
    #path('', views.home, name="home"),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]