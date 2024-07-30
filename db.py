from typing import List
from uuid import UUID

from models import Gender, Role, User

dbList: List[User] = [
    User(
        id=UUID("c623cdaa-25cb-4587-9235-7632292368ee"),
        first_name="Nina",
        last_name="Leonel",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("58caa553-51e5-4cd9-862a-63c2dcfbe10b"),
        first_name="Nathalia",
        last_name="Zeidan",
        gender=Gender.female,
        roles=[Role.user]
    ),
    User(
        id=UUID("da58330b-8de3-4928-9180-1b37d1031364"),
        first_name="Vinicius",
        last_name="Leonel",
        gender=Gender.male,
        roles=[Role.admin]
    )
]