from typing import re, Optional, List

from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure


def dish_measure_serializer(data: re) -> Optional[List[DishMeasure]]:
    try:
        dish_measures = [
            DishMeasure(
                id=data[i]['dish_measure_id'],
                price_value=data[i]['dish_measure_price_value'],
                measure_value=data[i]['dish_measure_measure_value'],
                dish_main=DishMain(id=data[i]['dish_measure_dish_main_id']))
            for i in range(len(data))
        ]
        return dish_measures
    except:
        raise TypeError


