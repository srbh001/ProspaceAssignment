import uuid
from django.db import models


ORDER_TYPE = [("Village", "Village"), ("District", "District"), ("Talluka", "Talluka")]


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order_type = models.CharField(
        choices=ORDER_TYPE, null=False, blank=False, max_length=255
    )
    entity_name = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(
        to="user_auth.CustomUser", on_delete=models.CASCADE, db_index=True
    )

    class Meta:
        ordering = ["-created_at"]


# NOTE: Test Models for now, change later on.


class Village(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    district = models.ForeignKey(to="District", on_delete=models.CASCADE, db_index=True)
    talluka = models.ForeignKey(to="Talluka", on_delete=models.CASCADE, db_index=True)
    data = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ["name"]


class District(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    data = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ["name"]


class Talluka(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    district = models.ForeignKey(to="District", on_delete=models.CASCADE, db_index=True)
    data = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ["name"]
