from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


class APPError(Exception):

    def __init__(self, err_code='APP_ERROR', err_message='Internal Server Error',
                 message='', status_code=status.HTTP_400_BAD_REQUEST):
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.status_code = status_code

    def __str__(self):
            return '[Error] %d: %s(%d)' % (self.err_code, self.err_message, self.status_code)

    def getResponse(self):
        return ErrorResponse(self.err_code, self.err_message, self.message, self.status_code)


def ErrorResponse(err_code='APP_ERROR', err_message='Internal Server Error',
                  message='', status=status.HTTP_400_BAD_REQUEST, headers=None):
    err = { 
        'error_code': err_code,
        'error': err_message,
        'message': message,
    }   
    return Response(err, status, headers=headers)
    
def custom_exception_handler(exc, context):

    if isinstance(exc, APPError):
        return ErrorResponse(exc.err_code, exc.err_message, exc.message, status=exc.status_code)
