from typing import re, List, Optional

from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain


def menu_category_serializer(data: re) -> Optional[List[MenuCategory]]:
    try:
        menu_categories = [
            MenuCategory(
                id=data[i]['menu_category_id'],
                name=data[i]['menu_category_name'],
                menu_main=MenuMain(id=data[i]['menu_category_menu_main_id'])
            )
            for i in range(len(data))
        ]
        return menu_categories
    except:
        raise TypeError
