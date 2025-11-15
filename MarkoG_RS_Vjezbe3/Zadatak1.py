import asyncio

async def fetch_list(lista):
    print("dohvacam listu sa weba...")
    await asyncio.sleep(3)
    print("gotov sa dohvacanjem")
    return lista

async def main():
    task1 = asyncio.create_task(fetch_list(lista=[broj for broj in range(1,11)]))
    result1 = await task1
    print("PODACI DOHVACENI")
    print(result1)

asyncio.run(main())