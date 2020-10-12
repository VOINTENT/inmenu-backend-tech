from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.dish_measure import DishMeasure

DES_DISH_MEASURE_ADD = 'dish-measure-add'


class DishMeasureDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_DISH_MEASURE_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(dish_measure_dict: dict) -> DishMeasure:
        return DishMeasure(
            price_value=dish_measure_dict['price_value'],
            measure_value=dish_measure_dict['measure_value']
        )
