import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    auth0_id = models.CharField(max_length=100, unique=True, editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_login = models.DateTimeField(null=True, editable=False)
    avatar = models.URLField(null=True)
