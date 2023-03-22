from django.contrib import admin
from . import models


admin.site.register(models.Beehive, list_display=("name", "description", "created"))
admin.site.register(models.Node, list_display=("vsn", "node_id", "beehive", "created", "registered", "owner"), list_filter=("beehive__name",), search_fields=("vsn", "node_id", "owner__username", "beehive__name"))
admin.site.register(models.NodeRegistrationToken, list_display=("key", "user", "beehive", "created", "expires"), search_fields=("user__username", "beehive__name"))
