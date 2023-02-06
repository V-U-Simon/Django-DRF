from django.urls import path

from .views import TailWindPageView

app_name = "app_theme"

urlpatterns = [
    path("", TailWindPageView.as_view(), name="tailwind"),
]
