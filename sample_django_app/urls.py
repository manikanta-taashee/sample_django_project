from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('all_users/', views.all_users, name='all_users')
]