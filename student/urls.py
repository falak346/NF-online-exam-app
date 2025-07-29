from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.student_login, name='student_login'),
    path('signup/', views.student_signup, name='student_signup'),
    path('dashboard/', views.st_index, name='st_index'),
    path('exam/<str:exam_id>/', views.attempt_exam, name='attempt_exam'),
    path('result/<str:exam_id>/', views.student_result, name='student_result'),
]
