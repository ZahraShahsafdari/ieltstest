from . import views
from django.urls import path

app_name = 'ieltstest'

urlpatterns = [
    path('reading_test/', views.reading, name='reading'),
    path('listening_test/', views.listening, name='listening'),
    path('writing_test/', views.writing, name='writing'),
 ]