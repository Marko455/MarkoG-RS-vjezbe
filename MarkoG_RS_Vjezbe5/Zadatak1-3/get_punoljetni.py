from aiohttp import web

korisnici = [
    {"ime": "Ana", "godine": 17},
    {"ime": "Ivan", "godine": 22},
    {"ime": "Marko", "godine": 18},
    {"ime": "Petra", "godine": 30},
    {"ime": "Luka", "godine": 16}
]

async def punoljetni(request):
    punoljetni_korisnici = [
        korisnik for korisnik in korisnici if korisnik["godine"] > 18
    ]

    return web.json_response(punoljetni_korisnici)

app = web.Application()
app.router.add_get("/punoljetni", punoljetni)

if __name__ == "__main__":
    web.run_app(app, port=8082)
