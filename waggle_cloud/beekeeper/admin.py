from django.contrib import admin
from . import models


class InstallationInline(admin.TabularInline):
    ordering = ("start",)
    model = models.Installation
    extra = 0


@admin.register(models.Beehive)
class BeehiveAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created")


@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("vsn", "node_id", "beehive", "notes")}),
        ("Registration", {"fields": ("registered", "owner")}),
    )
    list_display = ("vsn", "node_id", "beehive", "created", "registered", "owner")
    list_filter = ("beehive__name",)
    search_fields=("vsn", "node_id", "owner__username", "beehive__name")
    inlines = (InstallationInline,)
    list_select_related = True


@admin.register(models.NodeRegistrationToken)
class NodeRegistrationTokenAdmin(admin.ModelAdmin):
    list_display = ("key", "user", "beehive", "created", "expires")
    search_fields=("user__username", "beehive__name")
    list_select_related = True
