from pydantic import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()

ENV_VAR = os.getenv("ENVIORNMENT")

class LatokenSettings(BaseSettings):
    apiKey: str = ""
    apiSecret: str = b''
    
class TwillioSettings(BaseSettings):
    account_sid: str = ""
    auth_token: str = ""

class Settings(LatokenSettings,TwillioSettings):
    pass


settings = Settings()

