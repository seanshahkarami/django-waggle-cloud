# Generated by Django 4.1.7 on 2023-03-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecr", "0004_alter_app_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
