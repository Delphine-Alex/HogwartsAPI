from fastapi import APIRouter

from config.db import conn

from models.index import wizards
from schemas.index import Wizard

wizard = APIRouter()


@wizard.get('/')
async def read_data():
    return conn.execute(wizards.select()).fetchall()

@wizard.get('/{id}')
async def read_data(id: int):
    return conn.execute(wizards.select().where(wizards.c.id == id)).fetchall()

@wizard.post('/')
async def write_data(wizard: Wizard):
    conn.execute(wizards.insert().values(
        firstname=wizard.firstname,
        lastname=wizard.lastname,
        house=wizard.house
    ))
    return conn.execute(wizards.select()).fetchall()

@wizard.put('/{id}')
async def update_data(id:int, wizard: Wizard):
    conn.execute(wizards.update().values(
        firstname=wizard.firstname,
        lastname=wizard.lastname,
        house=wizard.house
    ).where(wizards.c.id == id))
    return conn.execute(wizards.select()).fetchall()

@wizard.delete('/{id}')
async def delete_data(id: int):
    conn.execute(wizards.delete().where(wizards.c.id == id))
    return conn.execute(wizards.select()).fetchall()