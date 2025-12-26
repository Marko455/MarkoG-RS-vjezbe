import aiohttp
import asyncio

async def main():
    amount = 12

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8086/cats/{amount}") as resp:
            cats_data = await resp.json()

        print(f"Dohvaćeno činjenica: {len(cats_data['facts'])}")

        async with session.post(
            "http://localhost:8087/facts",
            json=cats_data
        ) as resp:
            filtered_data = await resp.json()

        print("Provjerene činjenice:")
        for fact in filtered_data["facts"]:
            print("-", fact)

if __name__ == "__main__":
    asyncio.run(main())
