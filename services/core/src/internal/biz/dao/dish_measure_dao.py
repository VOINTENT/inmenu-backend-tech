from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.dish_measure import DishMeasure


class DishMeasureDao(BaseDao):

    async def add_many(self, dish_measures: List[DishMeasure]) -> Tuple[None, Optional[Error]]:
        sql = """
            INSERT INTO dish_measure(dish_main_id, price_value, measure_value) VALUES 
        """

        inserted_values = []
        for dish_measure, i in list(zip(dish_measures, range(1, len(dish_measures) * 3, 3))):
            sql += ', ' if len(inserted_values) != 0 else ''
            sql += f'(${i}, ${i + 1}, ${i + 2})'
            inserted_values.append(dish_measure.dish_main.id)
            inserted_values.append(dish_measure.price_value)
            inserted_values.append(dish_measure.measure_value)

        if inserted_values:
            await self.conn.execute(sql, *inserted_values)

        return None, None
