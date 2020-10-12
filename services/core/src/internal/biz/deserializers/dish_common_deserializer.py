from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.dish_main import DishMainDeserializer, DES_DISH_MAIN_ADD
from src.internal.biz.deserializers.dish_measures import DishMeasuresDeserializer, DES_DISH_MEASURES_ADD
from src.internal.biz.entities.dish_common import DishCommon

DES_DISH_COMMON_ADD = 'dish-common-add'


class DishCommonDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_DISH_COMMON_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(dish_common_dict: dict) -> DishCommon:
        return DishCommon(
            dish_main=DishMainDeserializer.deserialize(dish_common_dict, DES_DISH_MAIN_ADD),
            dish_measures=DishMeasuresDeserializer.deserialize(dish_common_dict['measures'], DES_DISH_MEASURES_ADD)
        )
