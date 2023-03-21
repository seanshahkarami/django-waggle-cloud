from django.apps import AppConfig


class EcrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "waggle_cloud.ecr"
    verbose_name = "Waggle Edge Code Repository"
