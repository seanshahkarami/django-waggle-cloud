from django.contrib import admin
from .models import App


admin.site.register(
    App,
    list_display=("name", "version", "description", "owner"),
    search_fields=("name", "owner__username"),
)
