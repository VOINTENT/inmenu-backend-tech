from typing import Optional

from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain


def menu_category_serializer(dictionary: dict) -> Optional[MenuCategory]:
    try:
        menu_category = MenuCategory(
                id=dictionary['menu_category_id'],
                name=dictionary['menu_category_name'],
                menu_main=MenuMain(id=dictionary['menu_category_menu_main_id'])
            )
        return menu_category
    except:
        raise TypeError
