from . import views
from django.urls import path

app_name = 'ieltstest'


urlpatterns = [
    path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('search/', views.search, name='search'),

    path('reading_test/', views.reading, name='reading'),
    path('listening_test/', views.listening, name='listening'),
    path('writing_test/', views.writing, name='writing'),
 ]