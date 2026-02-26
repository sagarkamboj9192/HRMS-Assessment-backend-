from typing import Optional
from hrm_backend.config.v1 import BaseSettingsWrapper


class PostgresConfig(BaseSettingsWrapper):

    POSTGRES_DB_NAME: str 
    POSTGRES_HOST: str 
    POSTGRES_USERNAME: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_PORT: Optional[int] = 5432

postgres_config = PostgresConfig()