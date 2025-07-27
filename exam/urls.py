from django.urls import path
from . import views

urlpatterns = [
    # Optional test view just to avoid the error
    path('test/', views.test_exam_view, name='test_exam'),
]
