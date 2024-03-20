from pydantic import BaseModel, field_validator
from src.enums.user_enums import Genders, Statuses, UsersErrors

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @field_validator("email")
    def check_that_dog_presented_in_email_addres(cls, email):
        if "@" in email:
            return email
        else:
            raise ValueError(UsersErrors.WRONG_EMAIL.value)