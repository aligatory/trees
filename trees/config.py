from pydantic import BaseSettings


class ServiceSettings(BaseSettings):
    address: str = "localhost"
    port: int = 8000


service_settings = ServiceSettings()
