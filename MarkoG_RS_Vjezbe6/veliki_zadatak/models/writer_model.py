from pydantic import BaseModel

class Writer(BaseModel):
    name: str
    surname: str