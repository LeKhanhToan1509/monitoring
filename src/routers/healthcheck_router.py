from fastapi import APIRouter
from response import *


healthRouter = APIRouter()

@healthRouter.get("/healthcheck")
def healthcheck():
    return ResponseHttp().getResponse(200, "OK")


    

