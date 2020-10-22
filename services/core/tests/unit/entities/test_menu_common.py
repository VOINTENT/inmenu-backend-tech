import pytest

from src.internal.biz.entities.currency import Currency
from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure
from src.internal.biz.entities.language import Language
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_common import MenuCommon
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.place_main import PlaceMain


def test_empty_init():
    menu_common = MenuCommon()

    assert menu_common.measure_unit is None
    assert menu_common.menu_category is None
    assert menu_common.dish_measures is None
    assert menu_common.currency is None
    assert menu_common.menu is None
    assert menu_common.dish_main is None
    assert menu_common.language is None


def test_correct_init_measure_unit():
    id = 1
    name = 'граммы'
    short_name = 'гр.'
    measure_unit = [MeasureUnit(
        id=id,
        name=name,
        short_name=short_name)]
    menu_common = MenuCommon(measure_units=measure_unit)

    assert menu_common.measure_unit[0].id == id
    assert menu_common.measure_unit[0].name == name
    assert menu_common.measure_unit[0].short_name == short_name


def test_correct_init_menu_category():
    id = 1
    menu_main = MenuMain(id=1, name='dish')
    name = 'name'
    menu_category = [MenuCategory(
        id=1,
        menu_main=menu_main,
        name=name,
    )]

    menu_common = MenuCommon(menu_categories=menu_category)

    assert menu_common.menu_category[0].id == id
    assert menu_common.menu_category[0].menu_main.id == menu_main.id
    assert menu_common.menu_category[0].menu_main.name == menu_main.name
    assert menu_common.menu_category[0].name == name


def test_correct_init_dish_measures():
    id = 1
    dish_main = DishMain(id=1, name='name')
    price_value = 40
    measure_value = 220

    dish_measure = [DishMeasure(id=id,
                                dish_main=dish_main,
                                price_value=price_value,
                                measure_value=measure_value)]

    menu_common = MenuCommon(dish_measures=dish_measure)

    assert menu_common.dish_measures[0].id == id
    assert menu_common.dish_measures[0].dish_main.id == dish_main.id
    assert menu_common.dish_measures[0].dish_main.name == dish_main.name
    assert menu_common.dish_measures[0].price_value == price_value
    assert menu_common.dish_measures[0].measure_value == measure_value


def test_correct_init_currency():
    id = 1
    name = 'name'
    short_nam = 'short_name'
    sign = 'sign'

    currency = Currency(
        id=id,
        name=name,
        short_name=short_nam,
        sign=sign
    )

    menu_common = MenuCommon(currency=currency)

    assert menu_common.currency.id == id
    assert menu_common.currency.name == name
    assert menu_common.currency.short_name is not None
    assert currency.short_name() == short_nam
    assert menu_common.currency.sign == sign


def test_correct_init_menu():
    id = 1
    name = 'name'
    place_main = PlaceMain(id=1, name='name')

    menu = MenuMain(id=id, name=name, place_main=place_main)

    menu_common = MenuCommon(main_menu=menu)

    assert menu_common.menu.id == id
    assert menu_common.menu.name == name
    assert menu_common.menu.place_main.id == place_main.id
    assert menu_common.menu.place_main.name == place_main.name


def test_correct_init_dish_main():
    id = 1
    name = 'name'

    dish_main = [DishMain(id=id,
                          name=name)]

    menu_common = MenuCommon(dishes_main=dish_main)

    assert menu_common.dish_main[0].id == id
    assert menu_common.dish_main[0].name == name


def test_correct_init_language():
    id = 1
    name = 'name'
    code_name = 'ru'

    language = Language(id=id,
                        name=name,
                        code_name=code_name)

    menu_common = MenuCommon(language=language)

    assert menu_common.language.id == id
    assert menu_common.language.name == name
    assert menu_common.language.code_name == code_name
