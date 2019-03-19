from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
    
def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

class DataUnavailable(APIException):
    status_code = 503
    default_detail = 'Some data missing, please check and try again.'
    default_code = 'data_unavailable'