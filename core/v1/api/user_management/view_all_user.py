from fastapi import APIRouter, Query, Response
from asgiref.sync import sync_to_async

from hrm_backend.models.v1.database.employee import Employee
from hrm_backend.models.v1.schemas.employee import EmployeeCreateResponse

router = APIRouter(tags=["authentication"])

@router.get("/view_all_employees")
async def get_all_employees(response: Response):
    try:
        employees = await sync_to_async(list)(
            Employee.objects.select_related("department").all()
        )

        employee_list = [
            {
                "id": emp.id,
                "full_name": emp.full_name,
                "email": emp.email,
                "department": emp.department.name if emp.department else None,
            }
            for emp in employees
        ]

        response.status_code = 200
        return EmployeeCreateResponse(
            status=True,
            message="Employees fetched successfully",
            data={"employees": employee_list},
            status_code=200,
        )

    except Exception as e:
        response.status_code = 400
        return EmployeeCreateResponse(
            status=False,
            message=f"Error in fetching employees: {str(e)}",
            data={},
            status_code=400,
        )