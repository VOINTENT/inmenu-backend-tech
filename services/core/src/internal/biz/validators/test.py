from marshmallow import Schema, fields

from src.internal.adapters.enums.validation_errors import ValidationErrorEnum


class TestSchema(Schema):
    test = fields.Str(required=True, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
