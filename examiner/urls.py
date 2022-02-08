from django.conf.urls import url
from . import views

urlpatterns = [
    url('examhome', views.addq, name='addq'),
    url('exam', views.exam, name='exam'),
    url('result', views.result, name='result'),
    url('logout', views.logout, name='logout'),
    url('exam', views.exam, name='exam'),
    url('comp',views.comp,name='comp'),
]