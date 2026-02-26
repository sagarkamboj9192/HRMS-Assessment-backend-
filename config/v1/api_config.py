from typing import Optional, List
from django.apps import AppConfig

from hrm_backend.config.v1 import BaseSettingsWrapper


class APIConfig(BaseSettingsWrapper):
    PROJECT_NAME: str = "hrm_backend"
    BACKEND_CORS_ORIGINS: List[str]=["http://localhost:5173","https://vite-react-ten-coral-37.vercel.app", "http://127.0.0.1:5173"]
    API_VER_STR_V1: str = "/api/v1"
    
    
api_config = APIConfig()

class DjangoAppConfig(AppConfig):
    name = api_config.PROJECT_NAME

    def ready(self):
        pass