import traceback
from inspect import isawaitable
from time import time

from src.extra.dao.log_request import LogRequestDao
from src.extra.entities.log_request import LogRequest
from src.internal.adapters.enums.errors import ErrorEnum


def log_request(func):
    async def wrapper(request, *args, **kwargs):

        start_time = time()
        try:
            response = func(request, *args, **kwargs)
            if isawaitable(response):
                response = await response
        except:
            err_message = traceback.format_exc()
            response = ErrorEnum.UNKNOWN_ERROR.get_response_with_error()
        else:
            err_message = None

        result_time = time() - start_time

        request_log = LogRequest(completion_time=result_time,
                                 method=request.method,
                                 url=request.url,
                                 ip=request.headers.get('x-real-ip'),
                                 status=response.status,
                                 error_msg=err_message)

        _, _ = await LogRequestDao().add(request_log)

        return response

    return wrapper
