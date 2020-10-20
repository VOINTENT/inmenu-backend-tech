from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_PLACE_MAIN_GET_MY = 'place-main-get-my'


class PlaceMainSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_PLACE_MAIN_GET_MY:
            return cls._serialize_get_my
        else:
            raise TypeError

    @staticmethod
    def _serialize_get_my(place_main: PlaceMain) -> dict:
        place_main.photo.create_full_url()
        return {
            'id': place_main.id,
            'name': place_main.name,
            'photo_link': place_main.photo.full_url
        }
