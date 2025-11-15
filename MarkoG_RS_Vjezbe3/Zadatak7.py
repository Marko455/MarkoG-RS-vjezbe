'''
Imamo tri korutine timer(name, delay) koje u petlji printaju preostale sekunde pa await asyncio.sleep(1) — dakle svaka 
 iteracija čeka 1 sekundu. U main() kreiramo tri zadatka (asyncio.create_task(...)) i onda await asyncio.gather(*timers)
 da čekamo da svi završe. asyncio.run(main()) pokreće event loop dok main() ne završi.

1. asyncio.run(main()) stvara novi event loop i radi loop.run_until_complete(main()).
2. U main() se poziva:
 timers = [
    asyncio.create_task(timer('Timer 1', 3)),
    asyncio.create_task(timer('Timer 2', 5)),
    asyncio.create_task(timer('Timer 3', 7))
]
3. Nakon kreiranja zadataka, main() poziva await asyncio.gather(*timers). To znači: main sada čeka da svi
 ti taskovi završe. Kontrolu prepušta event loop-u da izvrši te taskove.

Event loop pusti svaki task da se izvršava dok ne dođe do await (to je trenutak kad task predaje kontrolu i postaje suspendiran),
 upravlja vremenom buđenja (npr. sleep) i ponovno raspoređuje suspendirane taskove kad su spremni — u kodu 
   to rezultira izmjeničnim ispisima svakog timera svakih ~1 sekundu, sve skupa traje koliko najduži timer otprilike 7 sekundi.
'''