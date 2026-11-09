from dotenv import load_dotenv
from pydantic.settings import BaseSettings

load_dotenv("")
class Settings(BaseSettings):
    google_api_key: str
    google_client_secret: str
    google_refresh_token: str
    database_url: str
    classifier_model: str
    agent_model: str
    poll_interval: int
    dashboard_url: str
    dashboard_username: str
    dashboard_password: str
settings = Settings()