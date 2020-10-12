from marshmallow import Schema, fields
from marshmallow.validate import Length

from src.internal.adapters.enums.validation_errors import ValidationErrorEnum


class MeasureSchema(Schema):
    price_value = fields.Integer(required=True, allow_none=False)
    measure_value = fields.Integer(required=True, allow_none=False)


class DishCommonAddSchema(Schema):
    name = fields.String(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD}, validate=Length(max=100))
    photo_link = fields.String(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
    description = fields.String(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD}, validate=Length(max=1000))
    menu_id = fields.Integer(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
    category_id = fields.Integer(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
    measure_unit_id = fields.Integer(required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
    measures = fields.List(fields.Nested(MeasureSchema), required=True, allow_none=False, error_messages={'required': ValidationErrorEnum.NOT_FIELD})
