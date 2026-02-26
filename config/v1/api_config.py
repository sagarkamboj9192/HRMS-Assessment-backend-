from typing import Optional
from django.apps import AppConfig

from hrm_backend.config.v1 import BaseSettingsWrapper


class APIConfig(BaseSettingsWrapper):
    PROJECT_NAME: str = "hrm_backend"
    BACKEND_CORS_ORIGINS: Optional[str] = None
    API_VER_STR_V1: str = "/api/v1"
    
    
api_config = APIConfig()

class DjangoAppConfig(AppConfig):
    name = api_config.PROJECT_NAME

    def ready(self):
        pass