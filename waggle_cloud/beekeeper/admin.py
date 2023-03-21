from django.contrib import admin
from . import models


admin.site.register(models.Beehive, list_display=("name", "description", "created"))
admin.site.register(models.Node, list_display=("vsn", "created"))
admin.site.register(models.NodeRegistrationToken)
