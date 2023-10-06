from django.urls import path
from . import views

urlpatterns = [
    path('request_exams/', views.requestExams, name="request_exams" ),
]