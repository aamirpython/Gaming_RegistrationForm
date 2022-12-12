from pydantic import BaseModel
import uuid



class createuser(BaseModel):
    name : str
    email : str
    password :str

class loginuser(BaseModel):
    username : str
    password : str
    
class updateuser(BaseModel):
    id :uuid.UUID
    name : str
    email : str

class deleteuser(BaseModel):
    user_id : uuid.UUID


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"