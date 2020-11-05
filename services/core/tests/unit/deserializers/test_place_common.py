from assets.test_conf import DATA_1_CONTACTS, DATA_1_LOCATION, DATA_2_LOCATION, DATA_1_PLACE_MAIN
from src.internal.biz.deserializers.place_common import PlaceCommonDeserializer, DES_PLACE_COMMON_UPDATE
from src.internal.biz.deserializers.place_main import TEMP_GET_NULL_INT, TEMP_GET_NULL_STR


def test_des_update_place_main():
    data_1 = DATA_1_PLACE_MAIN

    data_2 = {'main_lang_id': None,
              "name": None,
              "description": None,
              "login": None,
              "photo_link": None,
              "main_currency_id": None}

    data_3 = {}

    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)
    place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)
    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)

    assert place_common_1.place_main.main_language.id == data_1['main_lang_id']
    assert place_common_1.place_main.name == data_1['name']
    assert place_common_1.place_main.login == data_1['login']
    assert place_common_1.place_main.description == data_1['description']
    assert place_common_1.place_main.photo.short_url == data_1['photo_link']
    assert place_common_1.place_main.main_currency.id == data_1['main_currency_id']

    assert place_common_2.place_main.main_language.id == TEMP_GET_NULL_INT
    assert place_common_2.place_main.name == TEMP_GET_NULL_STR
    assert place_common_2.place_main.description == TEMP_GET_NULL_STR
    assert place_common_2.place_main.login == TEMP_GET_NULL_STR
    assert place_common_2.place_main.photo.short_url == TEMP_GET_NULL_STR
    assert place_common_2.place_main.main_currency.id == TEMP_GET_NULL_INT

    assert place_common_3.place_main.main_language is None
    assert place_common_3.place_main.name is None
    assert place_common_3.place_main.description is None
    assert place_common_3.place_main.login is None
    assert place_common_3.place_main.photo is None
    assert place_common_3.place_main.main_currency is None


def test_des_update_place_contacts():
    data_1 = DATA_1_CONTACTS

    data_2 = {'contacts': {
        "phone_number": None,
        "email": None,
        "site_link": None,
        "facebook_link": None,
        "instagram_link": None,
        "vk_link": None,
    }
    }
    data_3 = {'contacts': {}}

    data_4 = {'contacts': None}

    data_5 = {}

    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)
    place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)
    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)
    place_common_4 = PlaceCommonDeserializer.deserialize(data_4, DES_PLACE_COMMON_UPDATE)
    place_common_5 = PlaceCommonDeserializer.deserialize(data_5, DES_PLACE_COMMON_UPDATE)

    assert place_common_1.place_contacts.vk_link == data_1['contacts']['vk_link']
    assert place_common_1.place_contacts.phone_number == data_1['contacts']['phone_number']
    assert place_common_1.place_contacts.email == data_1['contacts']['email']
    assert place_common_1.place_contacts.site_link == data_1['contacts']['site_link']
    assert place_common_1.place_contacts.facebook_link == data_1['contacts']['facebook_link']
    assert place_common_1.place_contacts.instagram_link == data_1['contacts']['instagram_link']
    assert place_common_1.place_contacts.id is None

    assert place_common_2.place_contacts.id is None
    assert place_common_2.place_contacts.vk_link == TEMP_GET_NULL_STR
    assert place_common_2.place_contacts.phone_number == TEMP_GET_NULL_STR
    assert place_common_2.place_contacts.email == TEMP_GET_NULL_STR
    assert place_common_2.place_contacts.site_link == TEMP_GET_NULL_STR
    assert place_common_2.place_contacts.facebook_link == TEMP_GET_NULL_STR
    assert place_common_2.place_contacts.instagram_link == TEMP_GET_NULL_STR

    assert place_common_3.place_contacts.id == TEMP_GET_NULL_INT
    assert place_common_3.place_contacts.vk_link is None
    assert place_common_3.place_contacts.phone_number is None
    assert place_common_3.place_contacts.email is None
    assert place_common_3.place_contacts.site_link is None
    assert place_common_3.place_contacts.facebook_link is None
    assert place_common_3.place_contacts.instagram_link is None

    assert place_common_4.place_contacts.id == TEMP_GET_NULL_INT
    assert place_common_4.place_contacts.vk_link is None
    assert place_common_4.place_contacts.phone_number is None
    assert place_common_4.place_contacts.email is None
    assert place_common_4.place_contacts.site_link is None
    assert place_common_4.place_contacts.facebook_link is None
    assert place_common_4.place_contacts.instagram_link is None

    assert place_common_5.place_contacts is None


def test_des_update_place_cuisine_type():
    data_1 = {'cuisine_types_ids': [1, 2, 3]}
    data_2 = {'cuisine_types_ids': [1]}
    data_3 = {'cuisine_types_ids': []}
    data_4 = {'cuisine_types_ids': None}
    data_5 = {}

    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)
    place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)
    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)
    place_common_4 = PlaceCommonDeserializer.deserialize(data_4, DES_PLACE_COMMON_UPDATE)
    place_common_5 = PlaceCommonDeserializer.deserialize(data_5, DES_PLACE_COMMON_UPDATE)


    assert isinstance(place_common_1.place_cuisine_types, list)
    assert place_common_1.place_cuisine_types[0].cuisine_type.id == data_1['cuisine_types_ids'][0]
    assert place_common_1.place_cuisine_types[1].cuisine_type.id == data_1['cuisine_types_ids'][1]
    assert place_common_1.place_cuisine_types[2].cuisine_type.id == data_1['cuisine_types_ids'][2]

    assert isinstance(place_common_2.place_cuisine_types, list)
    assert place_common_2.place_cuisine_types[0].cuisine_type.id == data_2['cuisine_types_ids'][0]

    assert isinstance(place_common_3.place_cuisine_types, list)
    assert place_common_3.place_cuisine_types[0].cuisine_type.id == TEMP_GET_NULL_INT

    assert isinstance(place_common_4.place_cuisine_types, list)
    assert place_common_4.place_cuisine_types[0].cuisine_type.id == TEMP_GET_NULL_INT

    assert place_common_5.place_cuisine_types is None

def test_des_update_place_place_type():
    data_1 = {'place_types_ids': [1, 2, 3]}
    data_2 = {'place_types_ids': [1]}
    data_3 = {'place_types_ids': []}
    data_4 = {'place_types_ids': None}
    data_5 = {}

    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)
    place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)
    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)
    place_common_4 = PlaceCommonDeserializer.deserialize(data_4, DES_PLACE_COMMON_UPDATE)
    place_common_5 = PlaceCommonDeserializer.deserialize(data_5, DES_PLACE_COMMON_UPDATE)

    assert isinstance(place_common_1.place_places_types, list)
    assert place_common_1.place_places_types[0].place_type.id == data_1['place_types_ids'][0]
    assert place_common_1.place_places_types[1].place_type.id == data_1['place_types_ids'][1]
    assert place_common_1.place_places_types[2].place_type.id == data_1['place_types_ids'][2]

    assert isinstance(place_common_2.place_places_types, list)
    assert place_common_2.place_places_types[0].place_type.id == data_2['place_types_ids'][0]

    assert isinstance(place_common_3.place_places_types, list)
    assert place_common_3.place_places_types[0].place_type.id == TEMP_GET_NULL_INT

    assert isinstance(place_common_4.place_places_types, list)
    assert place_common_4.place_places_types[0].place_type.id == TEMP_GET_NULL_INT

    assert place_common_5.place_places_types is None

def test_des_update_place_services():
    data_1 = {'services_ids': [1, 2, 3]}
    data_2 = {'services_ids': [1]}
    data_3 = {'services_ids': []}
    data_4 = {'services_ids': None}
    data_5 = {}

    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)
    place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)
    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)
    place_common_4 = PlaceCommonDeserializer.deserialize(data_4, DES_PLACE_COMMON_UPDATE)
    place_common_5 = PlaceCommonDeserializer.deserialize(data_5, DES_PLACE_COMMON_UPDATE)

    assert isinstance(place_common_1.place_services, list)
    assert place_common_1.place_services[0].service.id == data_1['services_ids'][0]
    assert place_common_1.place_services[1].service.id == data_1['services_ids'][1]
    assert place_common_1.place_services[2].service.id == data_1['services_ids'][2]

    assert isinstance(place_common_2.place_services, list)
    assert place_common_2.place_services[0].service.id == data_2['services_ids'][0]

    assert isinstance(place_common_3.place_services, list)
    assert place_common_3.place_services[0].service.id == TEMP_GET_NULL_INT

    assert isinstance(place_common_4.place_services, list)
    assert place_common_4.place_services[0].service.id == TEMP_GET_NULL_INT

    assert place_common_5.place_services is None

def test_des_update_place_location():
    data_1 = DATA_1_LOCATION

    data_2 = DATA_2_LOCATION

    data_3 = {'location': {}}
    data_4 = {'location': None}
    data_5 = {}

    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)

    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)
    place_common_4 = PlaceCommonDeserializer.deserialize(data_4, DES_PLACE_COMMON_UPDATE)
    place_common_5 = PlaceCommonDeserializer.deserialize(data_5, DES_PLACE_COMMON_UPDATE)

    assert place_common_1.place_location.id is None
    assert place_common_1.place_location.full_address == data_1['location']['full_address']
    assert place_common_1.place_location.city == data_1['location']['city']
    assert place_common_1.place_location.country == data_1['location']['country']
    assert place_common_1.place_location.coords == (data_1['location']['coords']['lat'], data_1['location']['coords']['long'])

    try:
        place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)
    except KeyError:
        assert 1 == 1

    assert place_common_3.place_location.id == TEMP_GET_NULL_INT
    assert place_common_3.place_location.full_address is None
    assert place_common_3.place_location.full_address is None
    assert place_common_3.place_location.city is None
    assert place_common_3.place_location.country is None
    assert place_common_3.place_location.coords is None

    assert place_common_4.place_location.id == TEMP_GET_NULL_INT
    assert place_common_4.place_location.full_address is None
    assert place_common_4.place_location.full_address is None
    assert place_common_4.place_location.city is None
    assert place_common_4.place_location.country is None
    assert place_common_4.place_location.coords is None

    assert place_common_5.place_location is None

def test_des_update_work_hours():
    data_1 = {"work_hours": {
        "mo": {
            "is_holiday": False,
            "is_all_day": False,
            "time_start": 28800,
            "time_finish": 79200
        }
    }
    }

    data_2 = {"work_hours": {
        "mo": {
            "is_holiday": False,
            "is_all_day": False,
            "time_start": 28800,
        }
    }
    }

    data_3 = {'work_hours': {}}

    data_4 = {'work_hours': None}
    data_5 = {}

    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)

    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)
    place_common_4 = PlaceCommonDeserializer.deserialize(data_4, DES_PLACE_COMMON_UPDATE)
    place_common_5 = PlaceCommonDeserializer.deserialize(data_5, DES_PLACE_COMMON_UPDATE)

    assert place_common_1.place_work_hours[0].week_day == 'mo'
    assert place_common_1.place_work_hours[0].is_holiday == data_1['work_hours']['mo']['is_holiday']
    assert place_common_1.place_work_hours[0].is_all_day == data_1['work_hours']['mo']['is_all_day']
    # assert place_common.place_work_hours[0].time_start == datetime.time(data_1['work_hours']['mo']['time_start'])
    # assert place_common.place_work_hours[0].time_finish == datetime.time(data_1['work_hours']['mo']['time_finish'])

    try:
        place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)
    except AttributeError:
        assert 1 == 1

    assert place_common_3.place_work_hours[0].id == TEMP_GET_NULL_INT
    assert place_common_3.place_work_hours[0].week_day is None
    assert place_common_3.place_work_hours[0].is_holiday is None
    assert place_common_3.place_work_hours[0].is_all_day is None
    assert place_common_3.place_work_hours[0].time_start is None
    assert place_common_3.place_work_hours[0].time_finish is None

    assert place_common_3.place_work_hours[0].id == TEMP_GET_NULL_INT
    assert place_common_4.place_work_hours[0].week_day is None
    assert place_common_4.place_work_hours[0].is_holiday is None
    assert place_common_4.place_work_hours[0].is_all_day is None
    assert place_common_4.place_work_hours[0].time_start is None
    assert place_common_4.place_work_hours[0].time_finish is None

    assert place_common_5.place_work_hours is None
