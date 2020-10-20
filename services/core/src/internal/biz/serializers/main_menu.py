from loguru import logger

from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_MENU_MAIN_SIMPLE = 'menu-main-simple'


class MenuMainSerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_MENU_MAIN_SIMPLE:
            return cls._serialize_simple
        else:
            raise TypeError

    @staticmethod
    def _serialize_simple(main_menu: MenuMain) -> dict:
        logger.debug(main_menu.photo.short_url)
        main_menu.photo.create_full_url()
        return {
            'id': main_menu.id,
            'name': main_menu.name,
            'photo_link': main_menu.photo.full_url
        }
