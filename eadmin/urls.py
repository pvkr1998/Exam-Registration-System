from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^adminhome/', views.adminhome, name='adminhome'),
    url(r'^addexam/', views.addexam, name='addexam'),
    url(r'^alogout/', views.alogout, name='alogout'),
    url(r'^adminprofile/', views.adminprofile, name='adminprofile'),
    url(r'^adminchangepassword/', views.adminchangepassword, name='adminchangepassword'),
    url(r'^addcourse/', views.addcourse, name='addcourse'),
    url(r'^accept/(?P<p1>\w+)/(?P<p2>\w+)/$', views.accept, name='accept'),

   # url(r'^accept/(?P<parameter>[\w-]+)', views.accept, name='accept'),
    url(r'^reject/(?P<p1>\w+)/(?P<p2>\w+)/$', views.reject, name='reject'),
]