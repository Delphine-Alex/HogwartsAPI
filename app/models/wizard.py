from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from database import Base

class WizardInfo(Base):
    __tablename__ = 'wizards'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    house = Column(String(100))
