from pydantic import BaseSettings


class ServiceSettings(BaseSettings):
    address: str = "localhost"
    port: int = 8000
    base_url: str = f"http://{address}:{port}"


service_settings = ServiceSettings()
