from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.dish_measure import DishMeasure
from src.internal.biz.entities.dish_main import DishMain
from src.internal.adapters.enums.errors import ErrorEnum



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

    async def get(self, menu_id):
        sql = """
            SELECT 
                dish_measure.id                     AS dish_measure_id,
                dish_measure.price_value            AS dish_measure_price_value,
                dish_measure.measure_value          AS dish_measure_measure_value,
                dish_measure.dish_main_id			AS dish_measure_dish_main_id
            FROM 
                dish_measure
            WHERE 
                dish_measure.dish_main_id IN(SELECT 
                                                    dish_main.id AS dish_main_id
                                            FROM 	
                                                dish_main	
                                            WHERE 
                                                dish_main.menu_main_id = $1)
                """
        if self.conn:
            data = await self.conn.fetch(sql, menu_id)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetch(sql, menu_id)
        if not data:
            return ErrorEnum.DISH_MEASURE_VALUE_AND_PRICE_DOESNT_EXISTS
        dish_measure = [
            DishMeasure(
                id=data[i]['dish_measure_id'],
                price_value=data[i]['dish_measure_price_value'],
                measure_value=data[i]['dish_measure_measure_value'],
                dish_main=DishMain(id=data[i]['dish_measure_dish_main_id']))
            for i in range(len(data))
        ]
        return dish_measure
