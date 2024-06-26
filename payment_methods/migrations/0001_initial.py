# Generated by Django 5.0.6 on 2024-05-08 01:59
import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PaymentMethod",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=500, null=True)),
                ("icon", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
