from django.urls import path

from .views import IndexPageView

app_name = "app_main"

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
]
