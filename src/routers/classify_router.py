from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from response import *
from requestModels import TenderPayload  
from controllers.classify_controller import classify_request_controller  
# Khởi tạo router
classifyRouter = APIRouter()

@classifyRouter.post("/classify")
async def classify_request(requestInput: TenderPayload):
    try:
        response = await classify_request_controller(requestInput) 
        return response
    except ValidationError as e:
        raise HTTPException(status_code=ResponseCode.UNPROCESSABLE_ENTITY.value, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=ResponseCode.INTERNAL_SERVER_ERROR.value, detail=f"Internal server error: {str(e)}")