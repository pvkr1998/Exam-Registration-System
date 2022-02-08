from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shome/', views.shome, name='shome'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^examregister/', views.examregister, name='examregister'),
    url(r'^mycourses/', views.mycourses, name='mycourses'),
    url(r'^hallticket/', views.hallticket, name='hallticket'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^password/', views.password, name='password'),
    url(r'^examht/(?P<parameter>[\w-]+)', views.examht, name='examht'),
    url(r'^pastexam/', views.pexam, name='pastexam'),
]