from fastapi import APIRouter, Request, Response, status, Query
from asgiref.sync import sync_to_async
from datetime import date
from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

from hrm_backend.models.v1.database.employee import Employee
from hrm_backend.models.v1.database.employee_attendance import Attendance
from hrm_backend.models.v1.schemas.employee_attendance import CreateAttendanceResponse

router = APIRouter(tags=["empolyee_details"])


@router.get("/view_all_attendance", status_code=status.HTTP_200_OK)
async def view_all_attendance(
    request: Request,
    response: Response,
    attendance_date: date = Query(..., description="Attendance date (YYYY-MM-DD)")
):
    try:
        
        attendance_exists = await sync_to_async(
            Attendance.objects.filter(date=attendance_date).exists
        )()

        if not attendance_exists:
            response.status_code = 200
            return CreateAttendanceResponse(
                status=True,
                message="No attendance data present on this date",
                data={},
                status_code=200,
            )
            
            
        attendance_subquery = Attendance.objects.filter(
            employee=OuterRef("pk"),
            date=attendance_date
        ).values("status")[:1]

        employees = await sync_to_async(list)(
            Employee.objects
            .select_related("department")
            .annotate(
                attendance_status=Coalesce(
                    Subquery(attendance_subquery),
                    Value("absent")
                )
            )
        )

        if not employees:
            response.status_code = 404
            return CreateAttendanceResponse(
                status=False,
                message="No employees found",
                data={},
                status_code=404,
            )

        employee_list = [
            {
                "employee_id": emp.id,
                "employee_name": emp.full_name,
                "email": emp.email,
                "department": emp.department.name if emp.department else None,
                "status": emp.attendance_status,
            }
            for emp in employees
        ]

        total_employees = len(employee_list)
        total_present = sum(
            1 for emp in employee_list if emp["status"] == "present"
        )
        total_absent = total_employees - total_present

        response.status_code = 200
        return CreateAttendanceResponse(
            status=True,
            message="Attendance fetched successfully",
            data={
                "attendance_date": attendance_date,
                "total_employees": total_employees,
                "total_present": total_present,
                "total_absent": total_absent,
                "employees": employee_list,
            },
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