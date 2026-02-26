from typing import Literal
from datetime import date
from pydantic import BaseModel

from hrm_backend.models.v1.schemas import Response

class CreateAttendanceRequest(BaseModel):
    employee_id: int
    date: date
    status: Literal["present", "absent"]

class CreateAttendanceResponse(Response):
    pass