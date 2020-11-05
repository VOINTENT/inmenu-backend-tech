from assets.test_conf import DATA_1_CONTACTS
from src.internal.biz.deserializers.place_common import DES_PLACE_COMMON_UPDATE, PlaceCommonDeserializer
from src.internal.biz.deserializers.place_contacts import PlaceContactsDeserializer, DES_PLACE_CONTACTS_UPDATE
from src.internal.biz.deserializers.place_main import TEMP_GET_NULL_STR, TEMP_GET_NULL_INT


def test_place_contacts_update():
    data_1 = DATA_1_CONTACTS
    place_contacts = PlaceContactsDeserializer.deserialize(data_1, DES_PLACE_CONTACTS_UPDATE)

    assert place_contacts.phone_number == data_1['phone_number']
    assert place_contacts.email == data_1['email']
    assert place_contacts.site_link == data_1['site_link']
    assert place_contacts.facebook_link == data_1['facebook_link']
    assert place_contacts.instagram_link == data_1['instagram_link']
    assert place_contacts.vk_link == data_1['vk_link']

    data_2 = {
        "phone_number": None,
        "email": None,
        "site_link": None,
        "facebook_link": None,
        "instagram_link": None,
        "vk_link": None,
    }
    place_contacts = PlaceContactsDeserializer.deserialize(data_2, DES_PLACE_CONTACTS_UPDATE)

    assert place_contacts.phone_number == TEMP_GET_NULL_STR
    assert place_contacts.email == TEMP_GET_NULL_STR
    assert place_contacts.site_link == TEMP_GET_NULL_STR
    assert place_contacts.facebook_link == TEMP_GET_NULL_STR
    assert place_contacts.instagram_link == TEMP_GET_NULL_STR
    assert place_contacts.vk_link == TEMP_GET_NULL_STR

    data_3 = {}

    place_contacts = PlaceContactsDeserializer.deserialize(data_3, DES_PLACE_CONTACTS_UPDATE)

    assert place_contacts.phone_number is None
    assert place_contacts.email is None
    assert place_contacts.site_link is None
    assert place_contacts.facebook_link is None
    assert place_contacts.instagram_link is None
    assert place_contacts.vk_link is None
