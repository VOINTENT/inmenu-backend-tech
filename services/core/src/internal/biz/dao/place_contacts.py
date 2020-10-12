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
