from src.internal.biz.deserializers.place_main import PlaceMainDeserializer, DES_PLACE_MAIN_UPDATE, TEMP_GET_NULL_INT, \
    TEMP_GET_NULL_STR


def test_place_main_deserialize_update():
    data = {"main_lang_id": 2,
            "name": "Хинкальная",
            "description": "Описание",
            "login": "hinkalka",
            "photo_link": "tmp/...",
            "main_currency_id": 2}
    place_main = PlaceMainDeserializer.deserialize(data, DES_PLACE_MAIN_UPDATE)

    assert data['main_lang_id'] == place_main.main_language.id
    assert data['name'] == place_main.name
    assert data['description'] == place_main.description
    assert data['login'] == place_main.login
    assert data['photo_link'] == place_main.photo.short_url
    assert data['main_currency_id'] == place_main.main_currency.id

    data = {'main_lang_id': None,
            "name": None,
            "description": None,
            "login": None,
            "photo_link": None,
            "main_currency_id": None}
    place_main = PlaceMainDeserializer.deserialize(data, DES_PLACE_MAIN_UPDATE)
    assert place_main.main_language.id == TEMP_GET_NULL_INT
    assert place_main.name == TEMP_GET_NULL_STR
    assert place_main.description == TEMP_GET_NULL_STR
    assert place_main.login == TEMP_GET_NULL_STR
    assert place_main.photo.short_url == TEMP_GET_NULL_STR
    assert place_main.main_currency.id == TEMP_GET_NULL_INT

    data = {}
    place_main = PlaceMainDeserializer.deserialize(data, DES_PLACE_MAIN_UPDATE)
    assert place_main.main_language == None
    assert place_main.name == None
    assert place_main.description == None
    assert place_main.login == None
    assert place_main.photo == None
    assert place_main.main_currency == None
