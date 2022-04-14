#obtained from https://stackoverflow.com/questions/60009296/django-3-0-channels-asgi-tokenauthmiddleware

from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser

from rest_framework.authtoken.models import Token


@database_sync_to_async
def get_user(headers):
    try:
        token_name, token_key = headers[b'authorization'].decode().split()
        if token_name == 'Token':
            token = Token.objects.get(key=token_key)
            print("token", token)
            return token.user
    except Token.DoesNotExist:
        print("no token")
        return AnonymousUser()


class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    # def __call__(self, scope):
    #     return TokenAuthMiddlewareInstance(scope, self)
    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers'])
        if b'authorization' in headers:
            scope['user'] = await get_user(headers)
        return await self.inner(scope, receive, send)


class TokenAuthMiddlewareInstance:
    """
    Yeah, this is black magic:
    https://github.com/django/channels/issues/1399
    """
    def __init__(self, scope, middleware):
        self.middleware = middleware
        self.scope = dict(scope)
        self.inner = self.middleware.inner

    async def __call__(self, receive, send):
        headers = dict(self.scope['headers'])
        if b'authorization' in headers:
            self.scope['user'] = await get_user(headers)
        inner = self.inner(self.scope)
        return await inner(receive, send)


TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
