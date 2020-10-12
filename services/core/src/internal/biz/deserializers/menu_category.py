from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain

DES_MENU_CATEGORY_ADD = 'menu-category-add'


class MenuCategoryDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_MENU_CATEGORY_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(menu_category_dict: dict) -> MenuCategory:
        return MenuCategory(
            name=menu_category_dict['name'],
            menu_main=MenuMain(id=menu_category_dict['menu_id'])
        )
