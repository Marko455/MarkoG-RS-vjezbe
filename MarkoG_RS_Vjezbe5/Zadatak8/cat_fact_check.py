from aiohttp import web
import re

async def check_facts(request):
    data = await request.json()
    facts = data.get("facts")

    if not facts:
        return web.json_response(
            {"error": "Lista činjenica nije proslijeđena"},
            status=400
        )

    return web.json_response({"facts": facts})


app = web.Application()
app.router.add_post("/facts", check_facts)

if __name__ == "__main__":
    web.run_app(app, port=8087)
