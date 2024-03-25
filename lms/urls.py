from django.urls import path

from lms.views import classes_view, class_view, assignments_view, assignment_view

urlpatterns = [
    path("classes", classes_view),
    path("class/<uuid:class_id>", class_view),
    path("assignments", assignments_view),
    path("assignment/<uuid:assignment_id>", assignment_view),
]
