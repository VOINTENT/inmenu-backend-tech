from typing import List, Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_location import PlaceLocation


class PlaceLocationDao(BaseDao):

    async def add_many(self, place_locations: List[PlaceLocation]) -> Tuple[None, Optional[Error]]:
        sql = """
            INSERT INTO place_location(place_main_id, full_location, coords) VALUES
        """

        inserted_values = []
        for place_location, i in list(zip(place_locations, range(1, len(place_locations) * 3, 3))):
            sql += ', ' if len(inserted_values) != 0 else ''
            sql += f'(${i}, ${i + 1}, ${i + 2})'
            inserted_values.append(place_location.place_main.id)
            inserted_values.append(place_location.full_address)
            inserted_values.append(place_location.coords)

        if inserted_values:
            await self.conn.execute(sql, *inserted_values)

        return None, None
