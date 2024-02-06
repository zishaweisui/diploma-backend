from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from infrastructure_exceptions import NotImplementedException


class TokensService:
    def __init__(self, jwt_secret, access_token_ttl, refresh_token_ttl):
        self.jwt_secret = jwt_secret
        self.access_token_ttl = access_token_ttl
        self.refresh_token_ttl = refresh_token_ttl

    def encode(self, token_type: str, data: dict):
        to_encode = data.copy()
        iat = datetime.now(tz=timezone.utc)
        match token_type:
            case "access":
                expire = datetime.now(tz=timezone.utc) + timedelta(minutes=self.access_token_ttl)
            case "refresh":
                expire = datetime.now(tz=timezone.utc) + timedelta(hours=self.refresh_token_ttl)
            case _:
                raise NotImplementedException
        to_encode.update(
            {
                "exp": expire,
                "iat": iat,
                "purpose": token_type
            }
        )
        encoded_jwt = jwt.encode(to_encode, self.jwt_secret, algorithm="HS256")
        return encoded_jwt

    def decode(self, token):
        try:
            payload = jwt.decode(
                token,
                self.jwt_secret,
                algorithms="HS256",
                options={
                    "require_iat": False,
                    "require_exp": False
                }
            )
        except JWTError:
            payload = None
        return payload
