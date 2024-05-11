import uuid

from django.db import models


class PaymentMethod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    icon = models.CharField(max_length=100, null=True)
