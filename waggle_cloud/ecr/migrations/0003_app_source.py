# Generated by Django 4.1.7 on 2023-03-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecr", "0002_app_description_app_repo_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="source",
            field=models.JSONField(default=dict),
        ),
    ]
