from django.urls import path

from .views import BootstrapPageView

app_name = "app_bootstrap"

urlpatterns = [
    path("", BootstrapPageView.as_view(), name="bootstrap"),
]
