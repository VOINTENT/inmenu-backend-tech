from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure
from src.internal.biz.serializers.entities_serializer.dish_measure_serializer import dish_measure_serializer


def test_dish_measure_serializer():
    data = {
        'dish_measure_id': 1,
        'dish_measure_price_value': 100,
        'dish_measure_measure_value': 200,
        'dish_measure_dish_main_id': 1,
    }
    dish_measure = DishMeasure(id=data['dish_measure_id'],
                               price_value=data['dish_measure_price_value'],
                               measure_value=data['dish_measure_measure_value'],
                               dish_main=DishMain(id=data['dish_measure_dish_main_id']))
    dish_measure_1 = dish_measure_serializer(data)

    assert isinstance(dish_measure, DishMeasure)
    assert isinstance(dish_measure_1, DishMeasure)

    assert isinstance(dish_measure.dish_main, DishMain)
    assert isinstance(dish_measure_1.dish_main, DishMain)

    assert dish_measure.id == dish_measure_1.id
    assert dish_measure.price_value == dish_measure_1.price_value
    assert dish_measure.measure_value == dish_measure_1.measure_value
    assert dish_measure.dish_main.id == dish_measure_1.dish_main.id