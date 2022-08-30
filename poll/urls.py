from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createpoll/', views.create_poll, name='createpoll'),
    path('poll_dashboard/', views.poll_statistics_dashboard, name='dashboard')
]
