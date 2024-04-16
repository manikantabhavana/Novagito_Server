# Generated by Django 5.0.4 on 2024-04-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_customer_industry_customer_output1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Query",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("mobile", models.CharField(max_length=10)),
                ("message", models.TextField()),
            ],
        ),
    ]
