from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_contacts import PlaceContacts


class PlaceContactsDao(BaseDao):

    async def add(self, place_contacts: PlaceContacts) -> Tuple[Optional[PlaceContacts], Optional[Error]]:
        await self.conn.execute(
            """
                INSERT INTO place_contacts(place_main_id, phone_number, email, site_link, vk_link, instagram_link, facebook_link)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
            """, place_contacts.place_main.id, place_contacts.phone_number, place_contacts.email, place_contacts.site_link,
            place_contacts.vk_link, place_contacts.instagram_link, place_contacts.facebook_link
        )
        return place_contacts, None

    async def update(self, place_main_id, place_contacts: PlaceContacts) -> Tuple[Optional[PlaceContacts], Optional[Error]]:
        sql = """
            UPDATE place_contacts
            SET
                phone_number = CASE WHEN $1::varchar != '-1' THEN $1::varchar WHEN $1::varchar = '-1' THEN NULL::varchar WHEN $1::varchar IS NULL THEN phone_number END,
                email = CASE WHEN $2::varchar != '-1' THEN $2::varchar WHEN $2::varchar = '-1' THEN NULL::varchar WHEN $2::varchar IS NULL THEN email END,
                site_link = CASE WHEN $3::varchar != '-1' THEN $3::varchar WHEN $3::varchar = '-1' THEN NULL::varchar WHEN $3::varchar IS NULL THEN site_link END,
                facebook_link = CASE WHEN $4::varchar != '-1' THEN $4::varchar WHEN $4::varchar = '-1' THEN NULL::varchar WHEN $4::varchar IS NULL THEN facebook_link END,
                instagram_link = CASE WHEN $5::varchar != '-1' THEN $5::varchar WHEN $5::varchar = '-1' THEN NULL::varchar WHEN $5::varchar IS NULL THEN instagram_link END,
                vk_link = CASE WHEN $6::varchar != '-1' THEN $6::varchar WHEN $6::varchar = '-1' THEN NULL::varchar WHEN $6::varchar IS NULL THEN vk_link END
            WHERE place_main_id = $7
        """
        await self.conn.execute(sql, place_contacts.phone_number if place_contacts.phone_number else None,
                                place_contacts.email if place_contacts.email else None,
                                place_contacts.site_link if place_contacts.site_link else None,
                                place_contacts.facebook_link if place_contacts.facebook_link else None,
                                place_contacts.instagram_link if place_contacts.instagram_link else None,
                                place_contacts.vk_link if place_contacts.vk_link else None,
                                place_main_id)
        return place_contacts, None

    async def delete(self, place_main_id: int):
        sql = f"""
        DELETE FROM place_contacts WHERE place_main_id = {place_main_id}"""
        await self.conn.execute(sql)
        return None, None

    async def get_check_by_id(self, place_main_id):
        sql = f"""
        SELECT 
            place_main_id AS place_main_id
        FROM
            place_contacts
        WHERE place_main_id = {place_main_id}
        """
        data = await self.conn.fetchval(sql)
        if not data:
            return False, None
        return True, None
