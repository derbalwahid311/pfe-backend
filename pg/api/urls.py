from django.urls import path
from .views import EnAPIView

urlpatterns = [
    path("en/", EnAPIView.as_view(), name=""),
]