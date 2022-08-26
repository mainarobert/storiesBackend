from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoute, name='routes'),
    path('stories', views.getStories, name='stories'),
    path('stories/<str:pk>', views.getStory, name='story')
]