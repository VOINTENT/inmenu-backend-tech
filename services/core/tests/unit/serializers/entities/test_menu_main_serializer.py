from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.serializers.entities_serializer.menu_main_serializer import menu_main_serializer


def test_menu_main_serializer():
    data = {
        'menu_main_id': 1,
        'menu_main_name': 'name',
        'menu_main_photo_link': 'photo',
        'menu_main_place_main_id': 1,
    }

    menu_main = MenuMain(
        id=data['menu_main_id'],
        name=data['menu_main_name'],
        photo=Photo(full_url=data['menu_main_photo_link']),
        place_main=PlaceMain(id=data['menu_main_place_main_id'])
    )

    menu_main_1 = menu_main_serializer(data)

    assert isinstance(menu_main, MenuMain)
    assert isinstance(menu_main_1, MenuMain)

    assert isinstance(menu_main.photo, Photo)
    assert isinstance(menu_main_1.photo, Photo)

    assert isinstance(menu_main.place_main, PlaceMain)
    assert isinstance(menu_main_1.place_main, PlaceMain)

    assert menu_main.id == menu_main_1.id
    assert menu_main.name == menu_main_1.name
    assert menu_main.photo.full_url == menu_main_1.photo.full_url
    assert menu_main.place_main.id == menu_main_1.place_main.id
