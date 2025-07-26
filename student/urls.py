from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.student_login, name='student_login'),
    path('exam/', views.take_exam, name='take_exam'),
    path('result/', views.view_result, name='view_result'),
]
