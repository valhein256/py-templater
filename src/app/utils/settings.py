"""Setting"""

from pydantic import BaseSettings

class Settings(BaseSettings):
    docs_url: str = None
    redoc_url: str = None
    openapi_url: str = None

    profile_enable: bool = False
    profile_name: str = None

    class Config:
        case_sensitive = True
        env_file_encoding = 'utf-8'
        fields = {
            'docs_url': {'env': 'API_SWAGGER'},
            'redoc_url': {'env': 'API_REDOC'},
            'openapi_url': {'env': 'API_OPENAPI_SCHEMA'},
            'profile_enable': {'env': 'PROFILE_ENABLE'},
            'profile_name': {'env': 'PROFILE_NAME'},
        }
