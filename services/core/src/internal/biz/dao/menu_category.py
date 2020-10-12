from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.menu_category import MenuCategory


class MenuCategoryDao(BaseDao):
    async def add(self, menu_category: MenuCategory) -> Tuple[Optional[MenuCategory], Optional[Error]]:
        async with self.pool.acquire() as conn:
            sql = """
                INSERT INTO menu_category(menu_main_id, name) VALUES ($1, $2)
                RETURNING id;
            """

            menu_category_id = await conn.fetchval(sql, menu_category.menu_main.id, menu_category.name)
            menu_category.id = menu_category_id
            return menu_category, None
