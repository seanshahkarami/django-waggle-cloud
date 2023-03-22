from django.contrib import admin
from . import models


admin.site.register(models.Beehive, list_display=("name", "description", "created"))
admin.site.register(models.Node, list_display=("vsn", "beehive", "created"), list_filter=("beehive__name",))
admin.site.register(models.NodeRegistrationToken, list_display=("key", "user", "beehive", "created", "expires"), search_fields=("user__username", "beehive__name"))
