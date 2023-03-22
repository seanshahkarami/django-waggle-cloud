from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"beehives", viewset=views.BeehiveViewSet)
router.register(r"nodes", viewset=views.NodeViewSet)
router.register(r"installations", viewset=views.InstallationViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
