from marshmallow import Schema, fields

from src.internal.adapters.enums.validation_errors import ValidationErrorEnum


class MenuCategoryAddSchema(Schema):
    menu_id = fields.Integer(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
    name = fields.String(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
