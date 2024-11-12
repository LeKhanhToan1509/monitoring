from fastapi import HTTPException
from pydantic import ValidationError
from response import ResponseCode  
from services import classify_request_logic 

async def classify_request_controller(requestInput):
    try:
        response = await classify_request_logic(requestInput)
        return response
    except ValidationError as e:
        raise HTTPException(status_code=ResponseCode.UNPROCESSABLE_ENTITY.value, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=ResponseCode.INTERNAL_SERVER_ERROR.value, detail=f"Internal server error: {str(e)}")