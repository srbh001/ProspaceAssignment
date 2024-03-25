import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from rest_framework.authtoken.models import Token


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    name = models.CharField("name", max_length=255)
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)
    date_joined = models.DateTimeField("date joined", default=datetime.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    grade = models.ForeignKey(
        to="lms.Class", on_delete=models.SET_NULL, null=True
    )  # Grade
    user_model = models.ForeignKey(
        to="authentication.CustomUser", on_delete=models.CASCADE
    )
    assignements = models.ManyToManyField(
        to="lms.Assignment",
        related_name="students",
    )  # Assignments assigned to student

    def __str__(self):
        return self.name


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    grade = models.ForeignKey(to="lms.Class", on_delete=models.CASCADE)  # Grade
    user_model = models.ForeignKey(
        to="authentication.CustomUser", on_delete=models.CASCADE
    )
    assignements = models.ManyToManyField(to="lms.Assignment", related_name="teachers")

    def __str__(self):
        return self.name
