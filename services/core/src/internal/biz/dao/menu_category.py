from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.deserializers.menu_category import MenuCategoryDeserializer, MENU_CATEGORY_ID, MENU_CATEGORY_NAME, \
    DES_MENU_CATEGORY_FROM_DB_FULL
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.serializers.entities_serializer.menu_category_serializer import menu_category_serializer


class MenuCategoryDao(BaseDao):
    async def add(self, menu_category: MenuCategory) -> Tuple[Optional[MenuCategory], Optional[Error]]:
        sql = """
            INSERT INTO menu_category(menu_main_id, name) VALUES ($1, $2)
            RETURNING id;
        """

        if self.conn:
            menu_category_id = await self.conn.fetchval(sql, menu_category.menu_main.id, menu_category.name)
            menu_category.id = menu_category_id
            return menu_category, None

        else:
            async with self.pool.acquire() as conn:
                menu_category_id = await conn.fetchval(sql, menu_category.menu_main.id, menu_category.name)
                menu_category.id = menu_category_id
                return menu_category, None

    async def get_by_menu_main_id(self, menu_main_id: int) -> Tuple[Optional[List[MenuCategory]], Optional[Error]]:
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(f"""
                SELECT
                    menu_category.id    AS {MENU_CATEGORY_ID},
                    menu_category.name  AS {MENU_CATEGORY_NAME}
                FROM
                    menu_category
                WHERE
                    menu_category.menu_main_id = $1
            """, menu_main_id)

            return [MenuCategoryDeserializer.deserialize(row, DES_MENU_CATEGORY_FROM_DB_FULL) for row in rows], None

    async def get(self, menu_id: int) -> Tuple[Optional[List[MenuCategory]], Optional[Error]]:
        sql = """
            SELECT 
                menu_category.id                    AS menu_category_id,
                menu_category.name                  AS menu_category_name,
                menu_category.menu_main_id          AS menu_category_menu_main_id
            FROM 
                menu_category
            WHERE
                menu_category.menu_main_id = $1
            """
        if self.conn:
            data = await self.conn.fetch(sql, menu_id)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetch(sql, menu_id)

        if not data:
            return None, ErrorEnum.MENU_CATEGORY_DOESNT_EXISTS

        menu_categories = [menu_category_serializer(dictionary) for dictionary in data]

        if not menu_categories:
            return None, ErrorEnum.MENU_CATEGORY_DOESNT_EXISTS

        return menu_categories, None
