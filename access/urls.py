from django.urls import path
from access.views import check_access

urlpatterns = [
    path("check/", check_access, name="check-access"),
]