from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.services import hash_password, check_password, generate_jwt

@api_view(["POST"])
def register(request):
    data = request.data

    user = User.objects.create(
        email=data["email"],
        password_hash=hash_password(data["password"])
    )

    return Response({"id": user.id})

@api_view(["POST"])
def login(request):
    data = request.data

    try:
        user = User.objects.get(email=data["email"], is_active=True)
    except User.DoesNotExist:
        return Response(status=401)

    if not check_password(data["password"], user.password_hash):
        return Response(status=401)
    
    token = generate_jwt(user.id)

    return Response({"access token": token})

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def me(request):
    if not request.jwt_user:
        return Response({"detail": "Unauthorized"}, status=401)

    return Response({
        "id": request.jwt_user.id,
        "email": request.jwt_user.email
    })