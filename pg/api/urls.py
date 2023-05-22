from django.urls import path
from .views import EnAPIView, EnseignantLogin, EngseignantView, EnseignantLogout

urlpatterns = [
    path("en/", EnAPIView.as_view(), name=""),
    path("login/", EnseignantLogin.as_view(), name="login"),
    path("logout/", EnseignantLogout.as_view(), name="logout"),
    path("user/", EngseignantView.as_view(), name="user"),
]