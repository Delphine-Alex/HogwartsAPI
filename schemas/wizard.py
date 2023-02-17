from pydantic import BaseModel

class Wizard(BaseModel):
    id: int
    firstname: str
    lastname: str
    house: str