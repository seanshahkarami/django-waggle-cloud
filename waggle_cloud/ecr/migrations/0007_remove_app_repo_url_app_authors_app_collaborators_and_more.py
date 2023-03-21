# Generated by Django 4.1.7 on 2023-03-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecr", "0006_app_updated"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="app",
            name="repo_url",
        ),
        migrations.AddField(
            model_name="app",
            name="authors",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="app",
            name="collaborators",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="app",
            name="funding",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="app",
            name="homepage",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="app",
            name="keywords",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="app",
            name="license",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="app",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]