from fastapi import APIRouter, Response, status
from asgiref.sync import sync_to_async

from hrm_backend.models.v1.database.employee import Department
from hrm_backend.models.v1.schemas.department import GetDepartmentResponse

router = APIRouter(tags=["empolyee_details"])

@router.get("/departments/dropdown", status_code=status.HTTP_200_OK)
async def get_departments_dropdown(response: Response):
    try:
        departments = await sync_to_async(list)(
            Department.objects.all().values("id", "name")
        )

        if not departments:
            response.status_code = 404
            return GetDepartmentResponse(
                status = False,
                message = "No departments found",
                data = {},
                status_code = 404
            )

        response.status_code = 200
        return GetDepartmentResponse(
            status = True,
            message = "Departments fetched successfully.",
            data = {"departments": departments},
            status_code = 200
        )

    except Exception as e:
        response.status_code = 400
        return {
            "status": False,
            "message": f"Error fetching departments: {str(e)}",
            "data": {},
            "status_code": 400
        }