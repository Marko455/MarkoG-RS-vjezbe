import asyncio

async def fetch_users():
    await asyncio.sleep(3)
    return [
        {"id": 1, "ime": "Ana"},
        {"id": 2, "ime": "Marko"},
    ]

async def fetch_products():
    await asyncio.sleep(5)
    return [
        {"id": 101, "proizvod": "Laptop"},
        {"id": 102, "proizvod": "Miš"},
    ]

async def main():
    users, products = await asyncio.gather(
        fetch_users(),
        fetch_products()
    )

    print("Korisnici:", users)
    print("Proizvodi:", products)

asyncio.run(main())

