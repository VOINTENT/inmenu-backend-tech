from src.internal.biz.entities.dish_common import DishCommon
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_DISH_COMMON_LIST = 'dish-common-list'


class DishCommonSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_DISH_COMMON_LIST:
            return cls._serialize_for_list
        else:
            raise TypeError

    @staticmethod
    def _serialize_for_list(dish_common: DishCommon) -> dict:
        dish_common.create_measure_price_str()
        dish_common.create_measure_measure_str()
        dish_common.dish_main.photo.create_full_url()
        return {
            'id': dish_common.dish_main.id,
            'name': dish_common.dish_main.name,
            'photo_link': dish_common.dish_main.photo.full_url,
            'dish_measure': {
                'price': dish_common.dish_measure_price_str,
                'measure': dish_common.dish_measure_measure_str
            }
        }
