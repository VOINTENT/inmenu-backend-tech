from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.account_status import AccountStatus
from src.internal.biz.entities.place_account_role import PlaceAccountRole


class PlaceAccountRoleDao(BaseDao):

    async def add(self, place_account_role: PlaceAccountRole) -> Tuple[Optional[PlaceAccountRole], Optional[Error]]:
        sql = """
            INSERT INTO place_account_role(place_main_id, account_main_id, account_status_id) VALUES 
            ($1, $2, $3);
        """

        await self.conn.execute(sql, place_account_role.place_main.id, place_account_role.account_main.id, place_account_role.account_status.id)

        return place_account_role, None

    async def get_by_menu_main_id(self, menu_main_id: int, auth_account_main_id) -> Tuple[Optional[PlaceAccountRole], Optional[Error]]:
        async with self.pool.acquire() as conn:
            sql = """
                SELECT account_status_id
                FROM menu_main INNER JOIN place_main ON menu_main.place_main_id = place_main.id INNER JOIN place_account_role ON place_main.id = place_account_role.place_main_id
                WHERE menu_main.id = $1 AND place_account_role.account_main_id = $2
            """

            status_id = await conn.fetchval(sql, menu_main_id, auth_account_main_id)

            if not status_id:
                return None, None

            return PlaceAccountRole(account_status=AccountStatus(id=status_id)), None

    async def get_by_place_main_id(self, place_main_id) -> Tuple[Optional[PlaceAccountRole], Optional[Error]]:
        sql = """
            SELECT 
                account_status.id, account_status.name
            FROM 
                place_account_role
            INNER JOIN 
                account_status ON place_account_role.account_status_id = account_status.id
            WHERE 
                place_main_id = $1
        """
        async with self.pool.acquire() as conn:
            status = await conn.fetchrow(sql, place_main_id)

        if not status:
            return None, ErrorEnum.STATUS_IS_UNDEFINED

        return PlaceAccountRole(account_status=AccountStatus(id=status[0], name=status[1])), None
