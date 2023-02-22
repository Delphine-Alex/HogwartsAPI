class WizardInfoException(Exception):
    ...


class WizardInfoNotFoundError(WizardInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Wizard Info Not Found"


class WizardInfoInfoAlreadyExistError(WizardInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Wizard Info Already Exists"