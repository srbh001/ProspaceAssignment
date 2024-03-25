import uuid
from django.db import models
from django.utils import choices


SECTION_CHOICES = (
    ("1", "Class 1"),
    ("2", "Class 2"),
    ("3", "Class 3"),
    ("4", "Class 4"),
    ("5", "lass 5"),
    ("s", "Class s"),
    ("7", "Class 7"),
    ("8", "Class 8"),
    ("9", "Class 9"),
    ("10", "Class 10"),
)


class Class(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section = models.CharField(choices=SECTION_CHOICES, max_length=20)

    def __str__(self) -> str:
        return self.section


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    teacher = models.ForeignKey(to="authentication.Teacher", on_delete=models.CASCADE)
    associated_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name="questions"
    )

    def __str__(self):
        return self.text
 