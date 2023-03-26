from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Beehive, Node, Installation


class BeehiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beehive
        fields = ["name", "description", "created"]


class NodeSerializer(serializers.ModelSerializer):
    beehive = serializers.CharField(source="beehive.name", read_only=True)

    class Meta:
        model = Node
        fields = ["vsn", "node_id", "beehive", "created", "registered"]


class InstallationSerializer(serializers.ModelSerializer):
    node = serializers.CharField(source="node.vsn", read_only=True)

    class Meta:
        model = Installation
        fields = ["node", "start", "end", "is_protected", "notes"]


class BeehiveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Beehive.objects.all()
    serializer_class = BeehiveSerializer
    permission_classes = [AllowAny]
    lookup_field = "name"


class NodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Node.objects.all().select_related("beehive")
    serializer_class = NodeSerializer
    permission_classes = [AllowAny]
    lookup_field = "vsn"


class InstallationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
    permission_classes = [AllowAny]


# TODO change default permission to something more locked down
