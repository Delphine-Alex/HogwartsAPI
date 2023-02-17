from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta

wizards = Table(
    'wizards', meta,
    
    Column('id', Integer, primary_key=True),
    Column('firstname', String(100)),
    Column('lastname', String(100)),
    Column('house', String(100)),
    
)