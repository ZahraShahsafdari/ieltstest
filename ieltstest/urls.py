from . import views
from .views import signin, signup, profile
from django.contrib.auth.views import LogoutView
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
    path('signin/', signin, name='signin'),
    path('signup/<str:email>/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='ieltstest:index'), name='logout'),

]