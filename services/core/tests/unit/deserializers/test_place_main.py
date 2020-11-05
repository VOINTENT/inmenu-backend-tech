from src.internal.biz.deserializers.place_main import PlaceMainDeserializer, DES_PLACE_MAIN_UPDATE, TEMP_GET_NULL_INT, \
    TEMP_GET_NULL_STR


def test_place_main_deserialize_update():
    data_1 = {"main_lang_id": 2,
            "name": "Хинкальная",
            "description": "Описание",
            "login": "hinkalka",
            "photo_link": "tmp/...",
            "main_currency_id": 2}
    place_main = PlaceMainDeserializer.deserialize(data_1, DES_PLACE_MAIN_UPDATE)

    assert data_1['main_lang_id'] == place_main.main_language.id
    assert data_1['name'] == place_main.name
    assert data_1['description'] == place_main.description
    assert data_1['login'] == place_main.login
    assert data_1['photo_link'] == place_main.photo.short_url
    assert data_1['main_currency_id'] == place_main.main_currency.id

    data_2 = {'main_lang_id': None,
            "name": None,
            "description": None,
            "login": None,
            "photo_link": None,
            "main_currency_id": None}
    place_main = PlaceMainDeserializer.deserialize(data_2, DES_PLACE_MAIN_UPDATE)
    assert place_main.main_language.id == TEMP_GET_NULL_INT
    assert place_main.name == TEMP_GET_NULL_STR
    assert place_main.description == TEMP_GET_NULL_STR
    assert place_main.login == TEMP_GET_NULL_STR
    assert place_main.photo.short_url == TEMP_GET_NULL_STR
    assert place_main.main_currency.id == TEMP_GET_NULL_INT

    data_3 = {}
    place_main = PlaceMainDeserializer.deserialize(data_3, DES_PLACE_MAIN_UPDATE)
    assert place_main.main_language is None
    assert place_main.name is None
    assert place_main.description is None
    assert place_main.login is None
    assert place_main.photo is None
    assert place_main.main_currency is None