import aiohttp
import asyncio

neki_brojevi = [2, 4, 6]

async def pozovi(url, payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            return await response.json()

async def main():
    payload = {"brojevi": neki_brojevi}

    zbroj_url = "http://localhost:8083/zbroj"
    umnozak_url = "http://localhost:8084/umnozak"

    zbroj_rez, umnozak_rez = await asyncio.gather(
        pozovi(zbroj_url, payload),
        pozovi(umnozak_url, payload)
    )

    print("zbroj:", zbroj_rez)
    print("Umnožak:", umnozak_rez)

    kolicnik_payload = {"zbroj": zbroj_rez["zbroj"], "umnozak": umnozak_rez["umnozak"]
    }

    kolicnik_url = "http://localhost:8085/kolicnik"
    kolicnik_rez = await pozovi(kolicnik_url, kolicnik_payload)

    print("Količnik:", kolicnik_rez)

if __name__ == "__main__":
    asyncio.run(main())
