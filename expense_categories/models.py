import uuid

from django.db import models


class ExpenseCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    icon = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=16, default="#FFFFFF")
