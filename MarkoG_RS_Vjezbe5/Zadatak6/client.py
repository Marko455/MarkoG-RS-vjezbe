import aiohttp
import asyncio

async def posalji_zahtjev(url, port):
    full_url = f"{url}:{port}/pozdrav"
    async with aiohttp.ClientSession() as session:
        async with session.get(full_url) as response:
            return await response.json()

async def main():
    odgovor1 = await posalji_zahtjev("http://localhost", 8081)
    odgovor2 = await posalji_zahtjev("http://localhost", 8082)

    print("Odgovor s mikroservisa 1:", odgovor1)
    print("Odgovor s mikroservisa 2:", odgovor2)

if __name__ == "__main__":
    asyncio.run(main())
