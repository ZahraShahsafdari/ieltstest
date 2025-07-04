from . import views
from django.urls import path

app_name = 'ieltstest'

urlpatterns = [
    path('reading_test/', views.reading, name='reading'),
 ]