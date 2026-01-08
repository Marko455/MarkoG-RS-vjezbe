from fastapi import FastAPI
from typing import List
import json

from models import filmovi_model as filmovi

app = FastAPI()

filmovi_db: List[filmovi] = []


@app.on_event("startup")
def load_films():
    with open("filmovi.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for film_data in data:
        film = Film(**film_data)
        filmovi_db.append(film)
