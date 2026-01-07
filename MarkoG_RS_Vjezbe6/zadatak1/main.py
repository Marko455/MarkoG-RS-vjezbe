from fastapi import FastAPI
from zadatak1.models import Film, CreateFilm

app = FastAPI()

filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

@app.get("/filmovi", response_model=list[Film])
def get_filmovi():
    return filmovi


@app.get("/filmovi/{id}", response_model=Film)
def get_film_by_id(id: int):
    for film in filmovi:
        if film["id"] == id:
            return film
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Film nije pronađen")


@app.post("/filmovi", response_model=Film)
def create_film(film: CreateFilm):
    new_id = max(f["id"] for f in filmovi) + 1 if filmovi else 1

    novi_film = {
        "id": new_id,
        "naziv": film.naziv,
        "genre": film.genre,
        "godina": film.godina
    }

    filmovi.append(novi_film)
    return novi_film


@app.get("/filmovi", response_model=list[Film])
def get_filmovi(genre: str | None = None, min_godina: int = 2000):
    rezultat = []

    for film in filmovi:
        if genre is not None and film["genre"] != genre:
            continue
        if film["godina"] < min_godina:
            continue
        rezultat.append(film)

    return rezultat
