import asyncio

async def secure_data(data):
    await asyncio.sleep(3)

    return {
        "prezime": data["prezime"],
        "broj_kartice": hash(str(data["broj_kartice"])),
        "CVV": hash(str(data["CVV"]))
    }

async def main():
    sensitive_list = [
        {"prezime": "Horvat", "broj_kartice": "1234-5678-9012-3456", "CVV": "321"},
        {"prezime": "Kovač", "broj_kartice": "4321-8765-2109-6543", "CVV": "123"},
        {"prezime": "Barić", "broj_kartice": "1111-2222-3333-4444", "CVV": "999"},
    ]

    tasks = [secure_data(entry) for entry in sensitive_list]

    results = await asyncio.gather(*tasks)

    for res in results:
        print(res)

asyncio.run(main())
