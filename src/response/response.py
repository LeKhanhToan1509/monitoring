from .httpCode import ResponseCode

class ResponseHttp:
    def __init__(self):
        pass

    @staticmethod
    def getResponse(code, data=None):
        if isinstance(code, ResponseCode):
            code_value = code.value 
            message = ResponseCode.get_message(code) 
        else:
            code_value = code
            message = "Unknown Status Code"
        
        return {
            "code": code_value,
            "message": message,
            "data": data
        }
