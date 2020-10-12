from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.currency import Currency
from src.internal.biz.entities.language import Language
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_main import PlaceMain

DES_PLACE_MAIN_ADD = 'place-main-add'


class PlaceMainDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_ser: str):
        if format_ser == DES_PLACE_MAIN_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(place_main: dict) -> PlaceMain:
        return PlaceMain(
            main_language=Language(id=place_main.get('main_lang_id')),
            name=place_main['name'] if place_main.get('name') else None,
            login=place_main['login'] if place_main.get('name') else None,
            photo=Photo(short_url=place_main['photo_link']) if place_main.get('photo_link') else None,
            description=place_main['description'] if place_main.get('description') else None,
            main_currency=Currency(id=place_main.get('main_currency_id')),
            is_draft=place_main['extra']['is_draft'],
            is_published=False
        )
