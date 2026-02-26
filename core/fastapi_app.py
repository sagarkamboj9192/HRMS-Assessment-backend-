from hrm_backend.core import connect_router

from hrm_backend.core.v1.api.user_management.create_user import (
    router as create_user_router_v1
)
from hrm_backend.core.v1.api.user_management.view_all_user import (
    router as view_all_user_router_v1
)
from hrm_backend.core.v1.api.user_management.delete_user import (
    router as delete_user_router_v1
)
from hrm_backend.core.v1.api.user_management.create_attendance import (
    router as create_attendance_router_v1
)
from hrm_backend.core.v1.api.user_management.view_all_attendance import (
    router as view_all_attendance_router_v1
)
from hrm_backend.core.v1.api.department.get_department import (
    router as get_department_router_v1
)

connect_router.include_router(create_user_router_v1)
connect_router.include_router(view_all_user_router_v1)
connect_router.include_router(delete_user_router_v1)
connect_router.include_router(create_attendance_router_v1)
connect_router.include_router(view_all_attendance_router_v1)
connect_router.include_router(get_department_router_v1)