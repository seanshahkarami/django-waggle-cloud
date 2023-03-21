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
        return reverse("app-detail", kwargs={"username": self.owner.username, "name": self.name, "version": self.version})
    
    def architectures(self):
        return self.source.get("architectures", [])

    def branch(self):
        return self.source.get("branch", "main")

    # NOTE DO NOT MIX AUTH, MAIL OR WHITENOISE HERE!!! WE MUST MAKE waggle_cloud composable!!!

    #   "name": "object-counter",
    #   "namespace": "yonghokim",
    #   "owner": "yonghokim",
    #   "science_description": "yonghokim/object-counter/0.5.1/ecr-science-description.md",

# {"architectures": ["linux/arm64"], "branch": "oneshot", "build_args": {"BUCKET_ID_MODEL": "3562bef2-735b-4a98-8b13-2206644bdb8e", "SAGE_STORE_URL": "https://osn.sagecontinuum.org"}, "directory": ".", "dockerfile": "Dockerfile", "git_commit": "2e0604d3a56a82ffbc2a5dba1e7f013f4debc09e", "tag": "", "url": "https://github.com/waggle-sensor/plugin-surface-water-detection"}
