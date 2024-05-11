from os import getenv

import requests
from authlib.jose import JoseError
from authlib.jose import jwt
from authlib.jose.rfc7517.jwk import JsonWebKey
from authlib.oauth2.rfc7523 import JWTBearerTokenValidator
from django.http import HttpResponse
from ninja.security import HttpBearer

from users.models import User


class Auth0JWTBearerTokenValidator(JWTBearerTokenValidator):
    def __init__(self, domain, audience):
        issuer = f"https://{domain}/"
        jsonurl = requests.get(f"{issuer}.well-known/jwks.json", timeout=10)
        public_key = JsonWebKey.import_key_set(jsonurl.json())
        super(Auth0JWTBearerTokenValidator, self).__init__(public_key)
        self.claims_options = {
            "exp": {"essential": True},
            "aud": {"essential": True, "value": audience},
            "iss": {"essential": True, "value": issuer},
        }

    def authenticate_token(self, token_string):
        try:
            claims = jwt.decode(
                token_string,
                self.public_key,
                claims_options=self.claims_options,
                claims_cls=self.token_cls,
            )
            claims.validate()
            return claims
        except JoseError as error:
            print("Authenticate token failed. %r", error)
            return None


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        auth0_token_validator = Auth0JWTBearerTokenValidator(
            domain=getenv("AUTH0_DOMAIN"),
            audience=getenv("AUTH0_AUDIENCE"),
        )
        claims = auth0_token_validator.authenticate_token(token_string=token)
        user = User.objects.filter(auth0_id=claims.get("sub")).first()
        if not user:
            return HttpResponse("Unauthorized", status=401)
        if claims and user:
            return token
