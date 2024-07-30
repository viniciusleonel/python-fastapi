from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List, Optional
from enum import Enum
    
class Role (str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
    
class Gender (str, Enum):
    male = "male"
    female = "female"

class User (BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]
    
class UserUpdateRequest (BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    roles: Optional[List[Role]] = None