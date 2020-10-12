from sanic.response import HTTPResponse

from src.internal.adapters.entities.validation_error import ValidationError
from src.internal.adapters.enums.validation_errors import ValidationErrorEnum


def get_response_with_validation_errors(errors: dict) -> HTTPResponse:
    errors_list = list(errors.items())

    # Всегда берем первую ошибку, если вернулось несколько
    error = errors_list[0]

    if error[0] == '_schema' and error[1] == ['Invalid input type.']:
        return ValidationErrorEnum.EMPTY_BODY.get_response_with_error()
    elif isinstance(error[1], ValidationError):
        return error[1].get_response_with_error(error[0])
    elif isinstance(error[1], dict):
        if isinstance(list(error[1].keys())[0], int):
            return get_response_with_validation_errors(error[1][list(error[1].keys())[0]])
        else:
            return get_response_with_validation_errors(error[1])
    elif isinstance(error[1], list):

        if isinstance(error[1][0], ValidationError):
            return error[1][0].get_response_with_error(error[0])
        elif isinstance(error[1][0], dict):
            if error[1][0].get('_schema') == ['Invalid input type.']:
                return ValidationErrorEnum.WRONG_TYPE_FIELD.get_response_with_error(error[0])
            return get_response_with_validation_errors(error[1][0])
        elif isinstance(error[1][0], str):
            if error[1][0] == 'Unknown field.':
                return ValidationErrorEnum.UNKNOWN_FIELD.get_response_with_error(error[0])
            elif error[1][0] == 'Field may not be null.':
                return ValidationErrorEnum.NULL_FIELD.get_response_with_error(error[0])
            else:
                return ValidationErrorEnum.WRONG_TYPE_FIELD.get_response_with_error(error[0])

    raise TypeError
