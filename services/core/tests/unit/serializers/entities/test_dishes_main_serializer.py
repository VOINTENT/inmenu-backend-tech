from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo
from src.internal.biz.serializers.entities_serializer.dish_main_serializer import dishes_main_serializer


def test_dishes_main_serializer():
    data = {
        'dish_main_id': 1,
        'dish_main_name': 'name',
        'dish_main_photo_link': 'photo_link',
        'dish_main_description': 'main_description',
        'dish_main_menu_main_id': 1,
        'dish_main_menu_category_id': 1,
        'dish_main_measure_unit_id': 1
    }
    dishes_main = dishes_main_serializer(data)
    dish_main = DishMain(id=data['dish_main_id'],
                         name=data['dish_main_name'],
                         photo=Photo(full_url=data['dish_main_photo_link']),
                         description=data['dish_main_description'],
                         menu_main=MenuMain(id=data['dish_main_menu_main_id']),
                         menu_category=MenuCategory(id=data['dish_main_menu_category_id']),
                         measure_unit=MeasureUnit(id=data['dish_main_measure_unit_id']))

    assert isinstance(dish_main, DishMain)
    assert isinstance(dishes_main, DishMain)

    assert isinstance(dish_main.photo, Photo)
    assert isinstance(dishes_main.photo, Photo)

    assert isinstance(dish_main.menu_main, MenuMain)
    assert isinstance(dishes_main.menu_main, MenuMain)

    assert isinstance(dish_main.menu_category, MenuCategory)
    assert isinstance(dishes_main.menu_category, MenuCategory)

    assert isinstance(dish_main.measure_unit, MeasureUnit)
    assert isinstance(dishes_main.measure_unit, MeasureUnit)

    assert dish_main.id == dishes_main.id
    assert dish_main.name == dishes_main.name
    assert dish_main.photo.full_url == dishes_main.photo.full_url
    assert dish_main.description == dishes_main.description
    assert dish_main.menu_main.id == dishes_main.menu_main.id
    assert dish_main.menu_category.id == dishes_main.menu_category.id
    assert dish_main.measure_unit.id == dishes_main.measure_unit.id
