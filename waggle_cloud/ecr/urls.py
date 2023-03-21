from django.urls import path
from . import views


urlpatterns = [
    path("apps/", views.AppListView.as_view(), name="app-list"),
    path("apps/<str:username>/", views.AppListForOwnerView.as_view()),
    path("apps/<str:username>/<str:name>/", views.AppListForOwnerAndNameView.as_view()),
    path("apps/<str:username>/<str:name>/<str:version>/", views.AppDetailView.as_view(), name="app-detail"),
]
