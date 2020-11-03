from src.internal.biz.deserializers.place_contacts import PlaceContactsDeserializer, DES_PLACE_CONTACTS_UPDATE
from src.internal.biz.deserializers.place_main import TEMP_GET_NULL_STR


def test_place_contacts_update():
    data = {
        "phone_number": "70000000000",
        "email": "email@mail.ru",
        "site_link": "http://hinkalka.ru",
        "facebook_link": "https://facebook.com/hinkalka",
        "instagram_link": "https://instagram.com/hinkalka",
        "vk_link": "https://vk.com/hinhalka"
    }
    place_contacts = PlaceContactsDeserializer.deserialize(data, DES_PLACE_CONTACTS_UPDATE)

    assert place_contacts.phone_number == data['phone_number']
    assert place_contacts.email == data['email']
    assert place_contacts.site_link == data['site_link']
    assert place_contacts.facebook_link == data['facebook_link']
    assert place_contacts.instagram_link == data['instagram_link']
    assert place_contacts.vk_link == data['vk_link']

    data = {
            "phone_number": None,
            "email":None,
            "site_link": None,
            "facebook_link": None,
            "instagram_link": None,
            "vk_link": None,
    }
    place_contacts = PlaceContactsDeserializer.deserialize(data, DES_PLACE_CONTACTS_UPDATE)

    assert place_contacts.phone_number == TEMP_GET_NULL_STR
    assert place_contacts.email == TEMP_GET_NULL_STR
    assert place_contacts.site_link == TEMP_GET_NULL_STR
    assert place_contacts.facebook_link == TEMP_GET_NULL_STR
    assert place_contacts.instagram_link == TEMP_GET_NULL_STR
    assert place_contacts.vk_link == TEMP_GET_NULL_STR

    data = {}

    place_contacts = PlaceContactsDeserializer.deserialize(data, DES_PLACE_CONTACTS_UPDATE)

    assert place_contacts.phone_number == None
    assert place_contacts.email == None
    assert place_contacts.site_link == None
    assert place_contacts.facebook_link == None
    assert place_contacts.instagram_link == None
    assert place_contacts.vk_link == None
