from aiohttp import web
import requests

AUTH0_DOMAIN = "your-tenant.auth0.com"

@web.middleware
async def auth_middleware(request, handler):
    if request.path == "/health":
        return await handler(request)

    auth = request.headers.get("Authorization")
    if not auth:
        raise web.HTTPUnauthorized(text="Missing Authorization header")

    token = auth.split()[1]

    # Call Auth0 userinfo endpoint
    response = requests.get(
        f"https://{AUTH0_DOMAIN}/userinfo",
        headers={"Authorization": f"Bearer {token}"}
    )

    if response.status_code != 200:
        raise web.HTTPUnauthorized(text="Invalid token")

    request["user"] = response.json()
    return await handler(request)
