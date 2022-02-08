from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ExamReg/', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
]