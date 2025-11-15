import asyncio
import random

async def provjeri_parnost(brojevi):
    rez = [f"Broj {broj} je paran" if broj%2!=0 else f"Broj {broj} nije paran." for broj in brojevi]
    await asyncio.sleep(2)
    return rez

async def main():
    brojevi = [random.randint(1,100) for _ in range(1,11)]
    task1 = asyncio.create_task(provjeri_parnost(brojevi))
    rezultat1 = await task1
    print(rezultat1)

asyncio.run(main())