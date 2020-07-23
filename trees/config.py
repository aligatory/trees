from pydantic import BaseSettings


class ServiceSettings(BaseSettings):
    address: str = "localhost"
    port: int = 8000
    access_key: str


service_settings = ServiceSettings()
