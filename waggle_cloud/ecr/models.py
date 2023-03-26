from django.conf import settings
from django.db import models
from django.urls import reverse


class App(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=16)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(default="")
    keywords = models.TextField(default="")
    authors = models.TextField(default="")
    collaborators = models.TextField(default="")
    funding = models.TextField(default="")
    license = models.TextField(default="")
    homepage = models.URLField(default="")
    source = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner}/{self.name}:{self.version}"

    def get_absolute_url(self):
        return reverse(
            "app-detail",
            kwargs={
                "username": self.owner.username,
                "name": self.name,
                "version": self.version,
            },
        )

    def architectures(self):
        return self.source.get("architectures", [])

    def branch(self):
        return self.source.get("branch", "main")
