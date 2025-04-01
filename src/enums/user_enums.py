from enum import Enum

class Genders(Enum):
    female = 'female'
    male = 'male'

class Statuses(Enum):
    active = 'active'
    inactive = 'inactive'

class UserErrors(Enum):
    WRONG_EMAIL_TEMPLATE = 'Email does not contain @'