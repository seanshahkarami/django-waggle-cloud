from django.conf import settings
from django.db import models
from secrets import token_hex
from datetime import timedelta


class Beehive(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Node(models.Model):
    vsn = models.CharField("VSN", max_length=8)
    node_id = models.CharField("Node ID", max_length=64)
    beehive = models.ForeignKey(Beehive, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    registered = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    notes = models.TextField(default="", blank=True)

    def __str__(self):
        return self.vsn


class Installation(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="installations")
    notes = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    is_protected = models.BooleanField(default=True)


def generate_node_registration_key():
    return token_hex(32)


class NodeRegistrationToken(models.Model):
    key = models.CharField(max_length=64, default=generate_node_registration_key, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    beehive = models.ForeignKey(Beehive, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DurationField(default=timedelta(days=7))
