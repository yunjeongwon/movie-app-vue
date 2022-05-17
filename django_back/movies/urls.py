from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.db_create, name='create'),
    path('<int:pk>/',views.detail, name='detail'),
]