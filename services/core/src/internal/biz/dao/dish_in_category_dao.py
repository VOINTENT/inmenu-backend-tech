from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.dish_measure import DishMeasure
from src.internal.biz.entities.count_dishes import CountDishes
from src.internal.adapters.enums.errors import ErrorEnum



class DishInCategoryDao(BaseDao):
    async def get(self, menu_id):
        sql = """
           SELECT  
               dish_main.menu_category_id   AS dish_main_menu_category_id,
               COUNT(dish_main.id)          AS count_dish_main_id_category
           FROM 
               dish_main
           WHERE 
               dish_main.menu_main_id = $1
           GROUP BY 
               dish_main.menu_category_id
               """
        if self.conn:
            data = await self.conn.fetch(sql, menu_id)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetch(sql, menu_id)
        if not data:
            return None, ErrorEnum.COUNT_DISH_IN_CATEGORY_DOESNT_EXISTS
        count_dish_in_category = [
            CountDishes(
                id=data[i]['dish_main_menu_category_id'],
                cnt=data[i]['count_dish_main_id_category']
            )
            for i in range(len(data))
            ]
        return count_dish_in_category