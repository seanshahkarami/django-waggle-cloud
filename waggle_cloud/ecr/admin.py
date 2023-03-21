from django.contrib import admin
from . import models


admin.site.register(models.App, list_display=("owner", "name", "version", "description"), search_fields=("owner__username", "name"))
