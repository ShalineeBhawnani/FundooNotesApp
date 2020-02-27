
import json
import re

from django.http import JsonResponse


def Smd_Response(success=False, message='something was wrong', data=[], status_code=400):
    smd = {
        'success': success,
        'message': message,
        'data': data,
    }
    response = JsonResponse(smd, status=status_code)
    return response


def smd_response(success=False, message='something was wrong', data=[]):
    smd = {
        'success': success,
        'message': message,
        'data': data,
    }
    return smd


