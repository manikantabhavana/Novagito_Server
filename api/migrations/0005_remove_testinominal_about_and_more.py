# Generated by Django 5.0.4 on 2024-04-14 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_testinominal_rename_customers_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="testinominal",
            name="about",
        ),
        migrations.RemoveField(
            model_name="testinominal",
            name="location",
        ),
        migrations.RemoveField(
            model_name="testinominal",
            name="mail",
        ),
    ]
