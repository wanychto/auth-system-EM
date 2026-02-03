import jwt
from django.conf import settings
from users.models import User
from django.utils.deprecation import MiddlewareMixin


class JWTAuthenticationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.jwt_user = None  # ← ВАЖНО

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=[settings.JWT_ALGORITHM],
            )
        except jwt.InvalidTokenError:
            return

        user_id = payload.get("user_id")

        try:
            user = User.objects.get(id=user_id, is_active=True)
        except User.DoesNotExist:
            return

        request.jwt_user = user