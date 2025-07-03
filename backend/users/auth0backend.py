# /app/users/auth0backend.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from jose import jwt
import requests

AUTH0_DOMAIN = "dev-7kw7hbs8zsir4onb.jp.auth0.com"
API_IDENTIFIER = "https://ia4c-api"
ALGORITHMS = ["RS256"]

User = get_user_model()

class Auth0JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization", None)
        if not auth_header:
            return None
        
        parts = auth_header.split()
        if parts[0].lower() != "bearer" or len(parts) != 2:
            raise AuthenticationFailed("Invalid Authorization header format.")

        token = parts[1]
        try:
            jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
            jwks = requests.get(jwks_url).json()
            unverified_header = jwt.get_unverified_header(token)

            rsa_key = {}
            for key in jwks["keys"]:
                if key["kid"] == unverified_header["kid"]:
                    rsa_key = {
                        "kty": key["kty"],
                        "kid": key["kid"],
                        "use": key["use"],
                        "n": key["n"],
                        "e": key["e"]
                    }
                    break

            if not rsa_key:
                raise AuthenticationFailed("Unable to find appropriate key.")

            # 一時的に audience 検証を無効化（必要に応じて戻す）
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                options={"verify_aud": False},
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
        except Exception as e:
            raise AuthenticationFailed(f"Invalid token: {e}")

        # 安全な値の取り出し
        # email = payload.get("email")
        email = payload.get("https://ia4c-api/email")
        # nickname = payload.get("nickname")

        if not email:
            raise AuthenticationFailed("Email not found in token.")

        username = nickname or email.split("@")[0]

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": username,
                "password": User.objects.make_random_password(),
            }
        )

        return (user, token)
