from fastapi import APIRouter, Query, Response
from asgiref.sync import sync_to_async

from hrm_backend.models.v1.database.employee import Employee
from hrm_backend.models.v1.schemas.employee import EmployeeCreateResponse

router = APIRouter(tags=["empolyee_details"])

@router.delete("/delete_employee")
async def delete_employee(
    response: Response,
    employee_id: int = Query(..., description="ID of the employee to delete")
):
    try:
        employee = await sync_to_async(
            Employee.objects.filter(id=employee_id).first
        )()

        if not employee:
            response.status_code = 404
            return EmployeeCreateResponse(
                status=False,
                message="Employee not found",
                data={},
                status_code=404,
            )

        await sync_to_async(employee.delete)()

        response.status_code = 200
        return EmployeeCreateResponse(
            status=True,
            message="Employee deleted successfully",
            data={"id": employee_id},
            status_code=200,
        )

    except Exception as e:
        response.status_code = 400
        return EmployeeCreateResponse(
            status=False,
            message=f"Error in deleting employee: {str(e)}",
            data={},
            status_code=400,
        )