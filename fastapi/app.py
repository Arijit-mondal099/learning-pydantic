from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class Setting(BaseModel):
    app_name: str = "Arijit"
    admin_email: str = "admin123@gmail.com"

def get_setting():
    return Setting()

@app.get("/")
def home():
    return {"message": "hello world!"}

@app.get("/settings")
def settings(settings: Setting = Depends(get_setting)): # Dependency injection
    return settings
