# Generated by Django 5.0.4 on 2024-04-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_remove_testinominal_about_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="industry",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="output1",
            field=models.CharField(
                blank=True, default="no content", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="output1_text",
            field=models.TextField(blank=True, default="no content", null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="output2",
            field=models.CharField(
                blank=True, default="no content", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="output2_text",
            field=models.TextField(blank=True, default="no content", null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="output3",
            field=models.CharField(
                blank=True, default="no content", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="output3_text",
            field=models.TextField(blank=True, default="no content", null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="problem",
            field=models.TextField(blank=True, default="no content", null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="solution",
            field=models.TextField(blank=True, default="no content", null=True),
        ),
    ]
