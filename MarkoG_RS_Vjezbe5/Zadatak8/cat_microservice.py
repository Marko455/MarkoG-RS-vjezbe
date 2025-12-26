from aiohttp import web, ClientSession
import asyncio

url = "https://catfact.ninja/fact"

async def fetch_fact(session):
    async with session.get(url) as response:
        data = await response.json()
        return data["fact"]

async def get_cats(request):
    try:
        amount = int(request.match_info["amount"])
    except ValueError:
        return web.json_response(
            {"error": "Amount mora biti cijeli broj"},
            status=400
        )

    async with ClientSession() as session:
        tasks = [fetch_fact(session) for _ in range(amount)]
        facts = await asyncio.gather(*tasks)

    return web.json_response({"facts": facts})


app = web.Application()
app.router.add_get("/cats/{amount}", get_cats)

if __name__ == "__main__":
    web.run_app(app, port=8086)
