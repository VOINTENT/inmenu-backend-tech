from marshmallow import Schema, fields
from marshmallow.validate import Length

from src.internal.adapters.enums.validation_errors import ValidationErrorEnum


class MenuAddSchema(Schema):
    place_id = fields.Integer(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
    name = fields.String(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
    photo_link = fields.String(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD}, validate=Length(min=1))
