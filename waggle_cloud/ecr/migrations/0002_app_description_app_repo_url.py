# Generated by Django 4.1.7 on 2023-03-21 00:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecr", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="app",
            name="repo_url",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
    ]
