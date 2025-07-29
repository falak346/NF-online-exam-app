from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.examiner_login, name='examiner_login'),
    path('signup/', views.examiner_signup, name='examiner_signup'),
    path('dashboard/', views.ex_index, name='ex_index'),
    path('batch/<str:batch_id>/', views.batch_detail, name='batch_detail'),
]
