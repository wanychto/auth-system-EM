from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from access.services import has_access
from access.models import Business_elements, Access_rules

@api_view(["GET"])
def check_access(request):
    user = getattr(request, "jwt_user", None)

    if not user:
        return Response({"detail": "Unauthorized"}, status=401)

    try:
        element = Business_elements.objects.get(name="orders")
    except Business_elements.DoesNotExist:
        return Response(
            {"detail": "Business element not found"},
            status=404
        )

    if not has_access(
        user=user,
        element=element,
        permission="read",
    ):
        return Response({"detail": "Forbidden"}, status=403)

    return Response({
        "data": "This is mock data for orders",
        "user": user.email
    })