from django.conf import settings
from django.db import models


class App(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=16)
    description = models.TextField()
    repo_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}/{self.name}:{self.version}"
