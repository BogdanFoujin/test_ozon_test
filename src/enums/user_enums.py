from enum import Enum

class Genders(Enum):
    female = "female"
    male="male"

class Statuses(Enum):
    inactive = "inactive"
    active = "active"

class UsersErrors(Enum):
    WRONG_EMAIL = "Email doesnt contain @"