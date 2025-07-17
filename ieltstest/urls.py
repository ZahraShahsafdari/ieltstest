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
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('skills/', views.skills, name='skills'),
    path('reading_test/<int:reading_text_id>/', views.reading_test, name='reading_test'),
    path('listening_test/<int:listening_text_id>/', views.listening_test, name='listening_test'),
    path('writinging_test/<int:writing_text_id>/', views.writing_test, name='writing_test'),
]