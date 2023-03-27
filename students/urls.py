from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name = 'student_registration')
]