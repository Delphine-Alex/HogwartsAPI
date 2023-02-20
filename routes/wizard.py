from typing import List
from sqlalchemy.orm import Session
from exceptions.exceptions import WizardInfoInfoAlreadyExistError, WizardInfoNotFoundError
from models.wizard import WizardInfo
from templates.wizard import CreateAndUpdateWizard

def get_wizards(session: Session, limit: int, offset: int) -> List[WizardInfo]:
    return session.query(WizardInfo).offset(offset).limit(limit).all()

# Function to  get info of a particular wizard
def get_wizard_by_id(session: Session, _id: int) -> WizardInfo:
    wizard_info = session.query(WizardInfo).get(_id)

    if wizard_info is None:
        raise WizardInfoNotFoundError

    return wizard_info

# Function to add a new  wizard info to the database
def create_wizard(session: Session, wizard_info: CreateAndUpdateWizard) -> WizardInfo:
    wizard_details = session.query(WizardInfo).filter(WizardInfo.firstname == wizard_info.firstname, WizardInfo.lastname == wizard_info.lastname, WizardInfo.house == wizard_info.house).first()
    if wizard_details is not None:
        raise WizardInfoInfoAlreadyExistError

    new_wizard_info = WizardInfo(**wizard_info.dict())
    session.add(new_wizard_info)
    session.commit()
    session.refresh(new_wizard_info)
    return new_wizard_info