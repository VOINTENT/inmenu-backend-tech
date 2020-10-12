from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.dao.dish_main_dao import DishMainDao
from src.internal.biz.dao.dish_measure_dao import DishMeasureDao
from src.internal.biz.entities.dish_common import DishCommon


class DishCommonDao(BaseDao):

    async def add(self, dish_common: DishCommon) -> Tuple[Optional[DishCommon], Optional[Error]]:
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                dish_main, err = await DishMainDao(conn).add(dish_common.dish_main)
                if err:
                    return None, err

                for dish_measure in dish_common.dish_measures:
                    dish_measure.dish_main = dish_main

                _, err = await DishMeasureDao(conn).add_many(dish_common.dish_measures)
                if err:
                    return None, err

                return dish_common, None
