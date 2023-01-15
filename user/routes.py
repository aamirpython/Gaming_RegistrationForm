from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi_login import LoginManager
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request,Form,status,Depends
from fastapi.responses import HTMLResponse,RedirectResponse
from pathlib import Path
from fastapi import FastAPI
from fastapi import APIRouter
from . models import *
from user.pydantic_models import createuser,loginuser,Token,updateuser,deleteuser
from passlib.context import CryptContext

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'user/templates')))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET = 'your-secret-key'
manager = LoginManager(SECRET, token_url='/auth/token')



@router.get("/home/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request,})

