from pydantic import BaseModel
from typing import List



class CreateAndUpdateWizard(BaseModel):
    firstname: str
    lastname: str
    house: str

class Wizard(CreateAndUpdateWizard):
    id: int

    class Config:
        orm_mode = True

class PaginatedWizardsInfo(BaseModel):
    limit: int
    offset: int
    data: List[Wizard]