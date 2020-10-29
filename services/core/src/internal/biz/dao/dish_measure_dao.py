from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.deserializers.dish_main import DISH_MAIN_ID
from src.internal.biz.deserializers.dish_measure import DISH_MEASURE_PRICE_VALUE, DISH_MEASURE_MEASURE_VALUE, \
    DISH_MEASURE
from src.internal.biz.deserializers.dish_measures import DishMeasuresDeserializer, DES_DISH_MEASURES_FROM_DB_FULL
from src.internal.biz.entities.dish_measure import DishMeasure

from src.internal.biz.entities.dish_measures import DishMeasures

from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.serializers.entities_serializer.dish_measure_serializer import dish_measure_serializer


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

    async def get_by_dish_main_ids(self, dish_main_ids: List[int]) -> Tuple[Optional[DishMeasures], Optional[Error]]:
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(f"""
                SELECT
                    DISTINCT ON (dish_measure.dish_main_id) dish_main_id    AS {DISH_MEASURE + DISH_MAIN_ID},
                    dish_measure.price_value                                AS {DISH_MEASURE_PRICE_VALUE},
                    dish_measure.measure_value                              AS {DISH_MEASURE_MEASURE_VALUE}
                FROM
                    dish_measure
                WHERE dish_measure.dish_main_id = ANY($1)
            """, dish_main_ids)

            return DishMeasuresDeserializer.deserialize(rows, DES_DISH_MEASURES_FROM_DB_FULL), None
