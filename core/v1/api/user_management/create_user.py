from django.core.validators import validate_email
from fastapi import APIRouter, Request, Response
from asgiref.sync import sync_to_async

from hrm_backend.models.v1.database.employee import Department, Employee
from hrm_backend.models.v1.schemas.employee import EmployeeCreateRequest,EmployeeCreateResponse

router = APIRouter(tags=["authentication"])

@router.post("/create_employees")
async def create_employee( 
    request: Request,
    body: EmployeeCreateRequest, 
    response: Response
    ):
    
    try:
        department = None
        
        _ = validate_email(value=body.email)

        employee_exist = await sync_to_async(Employee.objects.filter(email=body.email).exists)()
        if employee_exist:
            response.status_code=404
            return EmployeeCreateResponse(
                status=False,
                message="An employee already registered with this email id.",
                data={"credentials": body.email},
                status_code=404,
            )

        if body.department_id:
            department = await sync_to_async(
                Department.objects.filter(id=body.department_id).first
            )()

        if not department:
            response.status_code=404
            return EmployeeCreateResponse(
                status=False,
                message="Department not found",
                data={"credentials": body.email},
                status_code=404,
            )


        employee = await sync_to_async(Employee.objects.create)(
            full_name=body.full_name,
            email=body.email,
            department=department
        )

        response.status_code=200
        return EmployeeCreateResponse(
            status=True,
            message="Employee created successfully",
            data= {
                "id": employee.id,
                "full_name": employee.full_name,
                "email": employee.email,
                "department": employee.department.name if employee.department else None,
            },
            status_code=200,
        )
    
    except Exception as e:
        response.status_code = 400
        return EmployeeCreateResponse(
            status=False,
            message=f"Error in creating employee: {str(e)}",
            data={},
            status_code=400,
        )