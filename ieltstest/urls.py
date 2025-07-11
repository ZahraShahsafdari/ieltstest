from . import views
from django.urls import path

app_name = 'ieltstest'


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('guide/', views.guide, name='guide'),
    path('download/', views.download, name='download'),
    path('search/', views.search, name='search'),
    path('readingmore/', views.readingmore, name='readingmore'),
    path('writingmore/', views.writingmore, name='writingmore'),
    path('listeningmore/', views.listeningmore, name='listeningmore'),



    path('reading_test/', views.reading, name='reading'),
    path('listening_test/', views.listening, name='listening'),
    path('writing_test/', views.writing, name='writing'),
 ]