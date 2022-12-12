from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi_login import LoginManager
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import FastAPI
from fastapi import APIRouter
from . models import *
from user.pydantic_models import createuser,loginuser,Token,updateuser,deleteuser
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET = 'your-secret-key'
manager = LoginManager(SECRET, token_url='/auth/token')

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)



@router.post('/registration/')
async def create_user(data:createuser):
    if await User.exists(email=data.email):
        return {"message": "Email already exist"}

    else:
        add_user = await User.create(email=data.email,name=data.name, password = get_password_hash(data.password))
        return add_user


@manager.user_loader()
async def load_user(email:str):
    if await User.exists(email=email):
        user = await User.get(email=email)
        return user


@router.post('/login/', )
async def login(data:loginuser):
     
    
    email = data.username
    user = await load_user(email)
    
    if not user:
        return JSONResponse({'status':False,'message':'User not Registered'},status_code=403)
    elif not verify_password(data.password,user.password):
        return JSONResponse({'status':False,'message':'Invalid password'},status_code=403)
    print(user.id)
    access_token = manager.create_access_token(
        data={'sub':jsonable_encoder(user.email),"name":jsonable_encoder(user.name)}
    
    )
    '''test  current user'''
    
    
    new_dict = jsonable_encoder(user)
    new_dict.update({"access_token":access_token})
    return Token(access_token=access_token, token_type='bearer')


@router.get('/alluser/')
async def read_user():
    alluser = await User.all()
    return alluser    


@router.put("/update/")
async def update_user(data:updateuser):
        if await User.exists(id =data.id):
                user_obj = await User.filter(id = data.id).update(name = data.name,email= data.email)
                print(user_obj)
                return {"Update user"}
        


@router.delete("/delete/")
async def delete_user(data: deleteuser):
    delete_user = await User.filter(id=data.user_id).delete()
    return  {"user delete successfully"}
