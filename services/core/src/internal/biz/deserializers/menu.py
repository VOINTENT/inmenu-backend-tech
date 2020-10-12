from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_main import PlaceMain


DES_MENU_ADD = 'menu-add'


class MenuDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_MENU_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(menu_dict: dict):
        return MenuMain(
            name=menu_dict['name'] if menu_dict.get('name') else None,
            place_main=PlaceMain(id=menu_dict['place_id']) if menu_dict.get('place_id') else None,
            photo=Photo(short_url=menu_dict['photo_link']) if menu_dict.get('photo_link') else None
        )
