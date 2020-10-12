from typing import List, T

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer, DES_FROM_DICT
from src.internal.biz.entities.place_contacts import PlaceContacts

DES_PLACE_CONTACTS_ADD = 'place-contacts-add'


class PlaceContactsDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_FROM_DICT:
            return cls._deserializer_from_dict(PlaceContacts)
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(place_contacts: dict):
        return PlaceContacts(
            phone_number=place_contacts['phone_number'] if place_contacts.get('phone_number') else None,
            email=place_contacts['email'] if place_contacts.get('email') else None,
            site_link=place_contacts['site_link'] if place_contacts.get('site_link') else None,
            facebook_link=place_contacts['facebook_link'] if place_contacts.get('facebook_link') else None,
            instagram_link=place_contacts['instagram_link'] if place_contacts.get('instagram_link') else None,
            vk_link=place_contacts['vk_link'] if place_contacts.get('vk_link') else None
        )
