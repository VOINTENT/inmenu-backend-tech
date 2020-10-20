from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_MENU_CATEGORY_SIMPLE = 'menu-category-simple'


class MenuCategorySerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_MENU_CATEGORY_SIMPLE:
            return cls._deserialize_simple
        else:
            raise TypeError

    @staticmethod
    def _deserialize_simple(menu_category: MenuCategory) -> dict:
        return {
            'id': menu_category.id,
            'name': menu_category.name
        }
