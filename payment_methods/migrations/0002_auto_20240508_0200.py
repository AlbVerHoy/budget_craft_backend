# Generated by Django 5.0.6 on 2024-05-08 01:17
from django.db import migrations


def create_default_payment_methods(apps, schema_editor):
    PaymentMethod = apps.get_model("payment_methods", "PaymentMethod")
    db_alias = schema_editor.connection.alias
    default_payment_methods = {
        "Bank Account": "Linking your bank account for direct payments and transfers",
        "Debit Card": "A card linked to your bank account for point-of-sale transactions",
        "Credit Card": "Allows you to borrow money for purchases and pay it back later",
        "Cash": "Physical currency for in-person transactions",
        "PayPal": "An online payment platform that securely stores your payment information",
        "Mobile Payment Apps": "Use your smartphone for contactless payments (e.g., Apple Pay, Google Pay)",
        "Checks": "Traditional paper checks for bill payments",
        "Cryptocurrency": "Digital currencies for online transactions (e.g., Bitcoin, Ethereum)",
    }
    for name, description in default_payment_methods.items():
        PaymentMethod.objects.using(db_alias).create(name=name, description=description)


class Migration(migrations.Migration):

    dependencies = [
        ("payment_methods", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_default_payment_methods)]
