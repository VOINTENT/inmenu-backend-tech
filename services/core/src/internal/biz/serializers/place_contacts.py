from src.internal.biz.entities.place_contacts import PlaceContacts
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_CONTACTS_SIMPLE = 'place-contacts-simple'


class PlaceContactsSerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_CONTACTS_SIMPLE:
            return cls._serialize_simple
        else:
            raise TypeError

    @staticmethod
    def _serialize_simple(place_contacts: PlaceContacts) -> dict:
        return {
            'phone_number': place_contacts.phone_number,
            'email': place_contacts.email,
            'instagram_link': place_contacts.instagram_link,
            'site_link': place_contacts.site_link,
            'vk_link': place_contacts.vk_link,
            'facebook_link': place_contacts.facebook_link
        }
