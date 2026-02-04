from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from access.services import has_access

@api_view(["GET"])
def orders_list(request):
    user = request.jwt_user

    if not user:
        return Response(status=401)

    if not has_access(user, "orders", "read"):
        return Response(status=403)

    return Response([
        {"id": 1, "total": 100},
        {"id": 2, "total": 250},
    ])
