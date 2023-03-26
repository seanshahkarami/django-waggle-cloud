from rest_framework import serializers
from rest_framework import generics
from rest_framework import permissions
from .models import App


class AppSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.username", read_only=True)

    class Meta:
        model = App
        fields = "__all__"


class AppListView(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.AllowAny]


class AppListForOwnerView(generics.ListAPIView):
    serializer_class = AppSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return App.objects.filter(owner__username=self.kwargs["username"])


class AppListForOwnerAndNameView(generics.ListAPIView):
    serializer_class = AppSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return App.objects.filter(
            owner__username=self.kwargs["username"], name=self.kwargs["name"]
        )


class AppDetailView(generics.RetrieveAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        username = self.kwargs.get("username")
        name = self.kwargs.get("name")
        version = self.kwargs.get("version")
        return App.objects.get(owner__username=username, name=name, version=version)
