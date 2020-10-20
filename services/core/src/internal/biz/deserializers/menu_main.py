from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.photo import PHOTO, PhotoDeserializer, DES_PHOTO_FROM_DB_FULL
from src.internal.biz.deserializers.place_main import PLACE_MAIN, PlaceMainDeserializer, DES_PLACE_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.utils import filter_keys_by_substr
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_main import PlaceMain


DES_MENU_ADD = 'menu-add'
DES_MENU_MAIN_FROM_DB_FULL = 'menu-main-from-db-full'

MENU_MAIN = 'mm_'
MENU_MAIN_ID = MENU_MAIN + ID
MENU_MAIN_CREATED_AT = MENU_MAIN + CREATED_AT
MENU_MAIN_EDITED_AT = MENU_MAIN + EDITED_AT
MENU_MAIN_NAME = MENU_MAIN + 'nm'


class MenuMainDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_MENU_ADD:
            return cls._deserialize_add
        elif format_des == DES_MENU_MAIN_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(menu_dict: dict) -> MenuMain:
        return MenuMain(
            name=menu_dict['name'] if menu_dict.get('name') else None,
            place_main=PlaceMain(id=menu_dict['place_id']) if menu_dict.get('place_id') else None,
            photo=Photo(short_url=menu_dict['photo_link']) if menu_dict.get('photo_link') else None
        )

    @staticmethod
    def _deserialize_from_db_full(menu_main: dict) -> MenuMain:
        photo = filter_keys_by_substr(menu_main, PHOTO)
        place_main = filter_keys_by_substr(menu_main, PLACE_MAIN)
        return MenuMain(
            id=menu_main.get(MENU_MAIN_ID),
            created_at=menu_main.get(MENU_MAIN_CREATED_AT),
            edited_at=menu_main.get(MENU_MAIN_EDITED_AT),
            name=menu_main.get(MENU_MAIN_NAME),
            place_main=PlaceMainDeserializer.deserialize(place_main, DES_PLACE_MAIN_FROM_DB_FULL),
            photo=PhotoDeserializer.deserialize(photo, DES_PHOTO_FROM_DB_FULL)
        )
