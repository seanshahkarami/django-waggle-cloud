# Generated by Django 4.1.7 on 2023-03-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecr", "0007_remove_app_repo_url_app_authors_app_collaborators_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app",
            name="authors",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="app",
            name="collaborators",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="app",
            name="description",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="app",
            name="funding",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="app",
            name="homepage",
            field=models.URLField(default=""),
        ),
        migrations.AlterField(
            model_name="app",
            name="keywords",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="app",
            name="license",
            field=models.TextField(default=""),
        ),
    ]
