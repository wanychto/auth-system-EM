import bcrypt
import jwt
from datetime import datetime, timezone
from django.conf import settings

def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def check_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        password_hash.encode()
    )

def generate_jwt(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        'exp': datetime.now(tz=timezone.utc) + settings.JWT_EXPIRATION_DELTA
    }

    token = jwt.encode(payload=payload,
        key=settings.JWT_SECRET_KEY,
        algorithm =settings.JWT_ALGORITHM)
    return token