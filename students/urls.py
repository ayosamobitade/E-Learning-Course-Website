from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name = 'student_registration'),
    path('enroll-course/', views.StudentEnrollingCourseView.as_view(), name = 'student_enroll_course'),
]