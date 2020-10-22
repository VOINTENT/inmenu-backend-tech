from typing import Optional

from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure


def dish_measure_serializer(dictionary: dict) -> Optional[DishMeasure]:
    try:
        dish_measure = DishMeasure(
                id=dictionary['dish_measure_id'],
                price_value=dictionary['dish_measure_price_value'],
                measure_value=dictionary['dish_measure_measure_value'],
                dish_main=DishMain(id=dictionary['dish_measure_dish_main_id']))

        return dish_measure
    except:
        raise TypeError
