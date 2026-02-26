from fastapi import APIRouter, Request, Response, status
from asgiref.sync import sync_to_async

from hrm_backend.models.v1.database.employee_attendance import Attendance
from hrm_backend.models.v1.schemas.employee_attendance import CreateAttendanceResponse

router = APIRouter()

@router.get("/view_all_attendance", status_code=status.HTTP_200_OK)
async def view_all_attendance(
    request: Request,
    response: Response,
):
    try:
        queryset = Attendance.objects.select_related("employee").all()
        attendances = await sync_to_async(list)(queryset)

        if not attendances:
            response.status_code = 404
            return CreateAttendanceResponse(
                status=False,
                message="No attendance records found",
                data={},
                status_code=404,
            )

        data = [
            {
                "employee": attendance.employee.full_name,
                "employee_id": attendance.employee.id,
                "date": attendance.date,
                "status": attendance.status,
            }
            for attendance in attendances
        ]

        return CreateAttendanceResponse(
            status=True,
            message="Attendance fetched successfully",
            data=data,
            status_code=200,
        )

    except Exception as e:
        response.status_code = 400
        return CreateAttendanceResponse(
            status=False,
            message=f"Error in fetching attendance: {str(e)}",
            data={},
            status_code=400,
        )