from django.urls import path
from . import views

urlpatterns = [
    path('admin-signup/', views.admin_signup, name='admin_signup'),
    path('select-login/', views.select_login, name='select_login'),
    path('select-signup/', views.select_signup, name='select_signup'),
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]

