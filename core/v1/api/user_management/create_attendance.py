from fastapi import APIRouter, HTTPException, Request, Response, status
from asgiref.sync import sync_to_async
from django.db import IntegrityError

from hrm_backend.models.v1.database.employee import Employee
from hrm_backend.models.v1.database.employee_attendance import Attendance
from hrm_backend.models.v1.schemas.employee_attendance import CreateAttendanceRequest,CreateAttendanceResponse

router = APIRouter(tags=["empolyee_details"])

@router.post("/attendance/create", status_code=status.HTTP_201_CREATED)
async def create_attendance(
    request: Request,
    body: CreateAttendanceRequest, 
    response: Response
    ):

    try:
        employee = await sync_to_async(
            Employee.objects.filter(id=body.employee_id).first
        )()

        if not employee:
            response.status_code=404
            return CreateAttendanceResponse(
                status=False,
                message="Employee not found",
                data={},
                status_code=404,
            )

        if body.status not in ["present", "absent"]:
            response.status_code=400
            return CreateAttendanceResponse(
                status=False,
                message="Invalid status. Allowed values: present, absent",
                data={},
                status_code=400,
            )

        try:
            attendance = await sync_to_async(Attendance.objects.create)(
                employee=employee,
                date=body.date,
                status=body.status
            )
        except IntegrityError:
            response.status_code=400
            return CreateAttendanceResponse(
                status=False,
                message="Attendance already marked for this employee on this date",
                data={},
                status_code=400,
            )

        response.status_code=200
        return CreateAttendanceResponse(
            status=True,
            message="Attendance created successfully",
            data= {
                "employee_id":employee.id,
                "employee_name": employee.full_name,
                "date": attendance.date,
                "status": attendance.status
            },
            status_code=200,
        )
    except Exception as e:
        response.status_code = 400
        return CreateAttendanceResponse(
            status=False,
            message=f"Error in creating attendance: {str(e)}",
            data={},
            status_code=400,
        )