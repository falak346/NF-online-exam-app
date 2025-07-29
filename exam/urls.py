from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/public/<str:exam_id>/', views.public_leaderboard, name='public_leaderboard'),
    path('leaderboard/assigned/<str:exam_id>/', views.assigned_leaderboard, name='assigned_leaderboard'),
]
