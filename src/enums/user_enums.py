from enum import Enum

class Genders(Enum):
    FEMALE = "female"
    MALE="male"

class Statuses(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"

class UsersErrors(Enum):
    WRONG_EMAIL = "Email doesnt contain @"