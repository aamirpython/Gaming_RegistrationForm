from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from user import api as UserRoute
from user import routes as UserR
from configs.connection import DATABASE_URL 
from fastapi.staticfiles import StaticFiles


db_url = DATABASE_URL()



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(UserRoute.router, tags=["API"]),
app.include_router(UserR.router, tags=["Route"]),


register_tortoise(
    app,
    db_url=db_url,
    modules={'models': ['user.models']},
    generate_schemas=True,
    add_exception_handlers=True
)