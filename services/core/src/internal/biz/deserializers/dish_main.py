from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo

DES_DISH_MAIN_ADD = 'dish-main-add'


class DishMainDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_DISH_MAIN_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(dish_main_dict: dict) -> DishMain:
        return DishMain(
            name=dish_main_dict['name'],
            photo=Photo(short_url=dish_main_dict['photo_link']),
            description=dish_main_dict['description'],
            menu_main=MenuMain(id=dish_main_dict['menu_id']),
            menu_category=MenuCategory(id=dish_main_dict['category_id']),
            measure_unit=MeasureUnit(id=dish_main_dict['measure_unit_id'])
        )
