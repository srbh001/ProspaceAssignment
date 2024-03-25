from django.urls import path

from authentication.views import login_get_token, student_register, teacher_register

urlpatterns = [
    path("login/", login_get_token, name="login"),
    path("student/register/", student_register, name="Student Register"),
    path("teacher/register/", teacher_register, name="teacher_register"),
]
