from typing import Optional

from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_main import PlaceMain


def menu_main_serializer(data) -> Optional[MenuMain]:
    try:
        menu_main = MenuMain(
            id=data['menu_main_id'],
            name=data['menu_main_name'],
            photo=Photo(full_url=data['menu_main_photo_link']),
            place_main=PlaceMain(id=data['menu_main_place_main_id'])
        )
        return menu_main
    except:
        raise TypeError
