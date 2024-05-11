import uuid

from django.db import models

from expense_categories.models import ExpenseCategory
from payment_methods.models import PaymentMethod
from users.models import User


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    amount = models.FloatField()
    description = models.TextField(max_length=500)
    category = models.ForeignKey(to=ExpenseCategory, on_delete=models.DO_NOTHING)
    payment_method = models.ForeignKey(to=PaymentMethod, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    is_recurring = models.BooleanField(default=False)
    recurrence_frequency = models.CharField(max_length=100, null=True, blank=True)
    next_occurrence = models.DateField(null=True, blank=True)
    end_of_recurrence = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.date} {self.description}"
