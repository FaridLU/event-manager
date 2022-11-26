import traceback

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def generic_exception_handler(exception) -> Response:
    return exception_handler(exception, {})


def get_generic_exception_handler_status_code(exception) -> int:
    if generic_exception_handler(exception):
        return generic_exception_handler(exception).status_code
    else:
        return status.HTTP_500_INTERNAL_SERVER_ERROR


def get_error_response(exception) -> Response:
    response: Response = Response(
        {'status': 'error'},
        status=get_generic_exception_handler_status_code(exception),
        content_type="application/json",
    )
    try:
        if type(exception.detail) == list:
            response.data['message'] = [str(ex.__str__()) for ex in exception.detail]
        else:
            response.data['message'] = exception.detail

    except Exception as e:
        response.data['message'] = str(exception)

    if settings.SEND_ERROR_TRACEBACK_IN_RESPONSE:
        try:
            response.data['traceback'] = traceback.format_exc()
        except:
            response.data['traceback'] = 'Could not get traceback'

    return response


def get_success_response(status_code=status.HTTP_200_OK, **kwargs) -> Response:
    return Response(
        {'status': 'success', **kwargs},
        status=status_code,
        content_type="application/json",
    )
