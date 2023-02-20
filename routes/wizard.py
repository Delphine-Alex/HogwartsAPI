from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy import exc as sa_exc

from config.db import conn

from models.index import wizards
from schemas.index import Wizard

wizard = APIRouter()


@wizard.get('/wizards')
async def read_data():
    return conn.execute(wizards.select()).fetchall()

@wizard.get('/wizard/{id}')
async def read_data(id: int):
    result = conn.execute(wizards.select().where(wizards.c.id == id)).fetchone()
    if not result:
        raise HTTPException(status_code=400, detail="Wizard not found")
    return result

@wizard.post('/wizards')
async def write_data(wizard: Wizard):
    try:
        conn.execute(wizards.insert().values(
            firstname=wizard.firstname,
            lastname=wizard.lastname,
            house=wizard.house
        ))
        return conn.execute(wizards.select()).fetchall()
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))

@wizard.put('/wizard/{id}')
async def update_data(id:int, wizard: Wizard):
    try:
        conn.execute(wizards.update().values(
            firstname=wizard.firstname,
            lastname=wizard.lastname,
            house=wizard.house
        ).where(wizards.c.id == id))
        result = conn.execute(wizards.select().where(wizards.c.id == id)).fetchone()
        if not result:
            raise HTTPException(status_code=400, detail="Wizard not found")
        return result
    except sa_exc.DataError as e:
        raise HTTPException(status_code=400, detail=str(e))

@wizard.delete('/{id}')
async def delete_data(id: int):
    try:
        conn.execute(wizards.delete().where(wizards.c.id == id))
        result = conn.execute(wizards.select()).fetchall()
        if not result:
            raise HTTPException(status_code=400, detail="No more wizards in database")
        return result
    except sa_exc.DataError as e:
        raise HTTPException(status_code=400, detail=str(e))