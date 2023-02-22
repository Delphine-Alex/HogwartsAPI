# api.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from routes.wizard import get_wizards, get_wizard_by_id, create_wizard, update_wizard, delete_wizard
from database import get_db
from exceptions.exceptions import WizardInfoException
from templates.wizard import Wizard, CreateAndUpdateWizard, PaginatedWizardsInfo

router = APIRouter()

@cbv(router)
class Wizards:
    session: Session = Depends(get_db)

    # API to get the list of wizard info
    @router.get("/wizards", response_model=PaginatedWizardsInfo)
    def list_wizards(self, limit: int = 10, offset: int = 0):

        wizards_list = get_wizards(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": wizards_list}

        return response
    
    # API endpoint to add a wizard info to the database
    @router.post("/wizards")
    def add_wizard(self, wizard_info: CreateAndUpdateWizard):

        try:
            wizard_info = create_wizard(self.session, wizard_info)
            return wizard_info
        except WizardInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular wizard
@router.get("/wizards/{id}", response_model = Wizard)
def get_wizard_info(id: int, session: Session = Depends(get_db)):

    try:
        wizard_info = get_wizard_by_id(session, id)
        return wizard_info
    except WizardInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing wizard info
@router.put("/wizards/{id}", response_model = Wizard)
def update_wizard_by_id(id: int, new_info: CreateAndUpdateWizard, session: Session = Depends(get_db)):

    try:
        wizard_info = update_wizard(session, id, new_info)
        return wizard_info
    except WizardInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a wizard info from the database
@router.delete("/wizards/{id}")
def delete_wizard_by_id(id: int, session: Session = Depends(get_db)):

    try:
        return delete_wizard(session, id)
    except WizardInfoException as cie:
        raise HTTPException(**cie.__dict__)


