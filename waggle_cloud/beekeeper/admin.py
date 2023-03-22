from django.contrib import admin
from . import models


@admin.register(models.Beehive)
class BeehiveAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created")
    search_fields=("name",)


@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("vsn", "node_id", "beehive", "notes")}),
        ("Registration", {"fields": ("registered", "owner")}),
    )
    list_display = ("vsn", "node_id", "beehive", "created", "registered", "owner")
    list_filter = ("beehive__name",)
    list_select_related = True
    search_fields=("vsn", "node_id", "owner__username", "beehive__name")
    autocomplete_fields = ("beehive", "owner")


@admin.register(models.NodeRegistrationToken)
class NodeRegistrationTokenAdmin(admin.ModelAdmin):
    list_display = ("key", "user", "beehive", "created", "expires")
    list_filter = ("beehive__name",)
    list_select_related = True
    search_fields=("user__username", "beehive__name")
    autocomplete_fields = ("user", "beehive")


@admin.register(models.Installation)
class InstallationAdmin(admin.ModelAdmin):
    list_display = ("node", "start", "end", "is_protected", "notes")
    list_filter = ("is_protected",)
    list_select_related = True
    search_fields=("node__vsn", "node__vsn")
    autocomplete_fields = ("node",)
