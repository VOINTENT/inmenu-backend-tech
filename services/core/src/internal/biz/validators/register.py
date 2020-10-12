from marshmallow import Schema, fields

from src.internal.adapters.enums.validation_errors import ValidationErrorEnum


class RegisterAuthSchema(Schema):
    email = fields.Str(required=True, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
    password = fields.Str(required=True, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
