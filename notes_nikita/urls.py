from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_views_nikita,name = 'notes_views_nikita'),

]