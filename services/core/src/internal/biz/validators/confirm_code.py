from marshmallow import Schema, fields, ValidationError

from src.internal.adapters.enums.validation_errors import ValidationErrorEnum


def validate_code(value: str):
    if len(value) != 6 or not value.isdigit():
        raise ValidationError([ValidationErrorEnum.WRONG_CODE_FORMAT])


class ConfirmCodeSchema(Schema):
    code = fields.Str(required=True, error_messages={'required': ValidationErrorEnum.NOT_FIELD}, validate=validate_code)
