from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.serializers.entities_serializer.menu_category_serializer import menu_category_serializer


def test_menu_category_serializer():
    data = {
        'menu_category_id': 1,
        'menu_category_name': 'name',
        'menu_category_menu_main_id': 1,
    }

    menu_category = MenuCategory(
        id=data['menu_category_id'],
        name=data['menu_category_name'],
        menu_main=MenuMain(id=data['menu_category_menu_main_id'])
    )

    menu_category_1 = menu_category_serializer(data)

    assert isinstance(menu_category, MenuCategory)
    assert isinstance(menu_category_1, MenuCategory)

    assert isinstance(menu_category.menu_main, MenuMain)
    assert isinstance(menu_category_1.menu_main, MenuMain)

    assert menu_category.id == menu_category_1.id
    assert menu_category.name == menu_category_1.name
    assert menu_category.menu_main.id == menu_category_1.menu_main.id