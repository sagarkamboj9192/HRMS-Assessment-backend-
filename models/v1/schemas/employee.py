from pydantic import BaseModel, EmailStr
from typing import Optional

from hrm_backend.models.v1.schemas import Response


class EmployeeCreateRequest(BaseModel):
    full_name: str
    email: EmailStr
    department_id: int
    
    class Config:
        from_attributes = True
        extra = "forbid"

class EmployeeCreateResponse(Response):
    pass