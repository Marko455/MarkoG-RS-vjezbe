from typing import List
from pydantic import BaseModel


class Film(BaseModel):
    title: str
    year: str
    rated: str
    released: str
    runtime: str
    genre: str
    director: str
    writer: str
    actors: str
    plot: str
    language: str
    country: str
    awards: str
    poster: str
    metascore: str
    imdbRating: str
    imdbVotes: str
    imdbID: str
    type: str
    response: str
    images: List[str]
