from pydantic import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()

ENV_VAR = os.getenv("ENVIORNMENT")

class LatokenSettings(BaseSettings):
    apiKey: str = "25c0bf96-a2d4-4679-88b9-48c35efd3120"
    apiSecret: str = b'MmFiZTJlY2YtOGM1Mi00NTA0LTlkYmItODljODA5M2NiMWJj'
    
class TwillioSettings(BaseSettings):
    account_sid: str = "AC62b5f1f188b3dfe453b9acb713cf9e7a"
    auth_token: str = "e4b27bf0cba4b64f9d40d2bfbdb07b95"

class Settings(LatokenSettings,TwillioSettings):
    pass


settings = Settings()

