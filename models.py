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
    id: Optional[UUID or str] = uuid4() # type: ignore
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]