from django.contrib import admin
from django.urls import path
from .views import ProjectListView, ProjectDetailView
from . import views


urlpatterns = [
    path('', views.home, name='website-home'),
    path('home/', views.home, name='website-home'),
    path('projects/', views.projects, name='website-projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-details'),
    path('about/', views.about, name='website-about'),
]
