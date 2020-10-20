from marshmallow import Schema, fields, ValidationError

from src.internal.adapters.enums.validation_errors import ValidationErrorEnum


def validate_email(value: str):
    if not value.find('@gmail.com'):
        raise ValidationError([ValidationErrorEnum.NOT_GMAIL])


class AuthGmailSchema(Schema):
    email = fields.Email(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD}, validate=validate_email)
    auth_code = fields.String(required=False, allow_none=False)
