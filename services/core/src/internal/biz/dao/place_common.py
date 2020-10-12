from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.dao.menu_main import MenuMainDao
from src.internal.biz.dao.place_account_role import PlaceAccountRoleDao
from src.internal.biz.dao.place_contacts import PlaceContactsDao
from src.internal.biz.dao.place_cuisine_type_dao import PlaceCuisineTypeDao
from src.internal.biz.dao.place_location import PlaceLocationDao
from src.internal.biz.dao.place_main_dao import PlaceMainDao
from src.internal.biz.dao.place_place_type import PlacePlaceTypeDao
from src.internal.biz.dao.place_service_dao import PlaceServiceDao
from src.internal.biz.dao.place_work_hours import PlaceWorkHoursDao
from src.internal.biz.entities.account_status import AccountStatus
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_account_role import PlaceAccountRole
from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.entities.place_main import PlaceMain

COMMON_MENU_NAME = 'Основное'


class PlaceCommonDao(BaseDao):

    async def add(self, place_common: PlaceCommon) -> Tuple[Optional[PlaceCommon], Optional[Error]]:
        async with self.pool.acquire() as conn:
            async with conn.transaction():

                place_main_dao = PlaceMainDao(conn)
                place_main, err = await place_main_dao.add(place_common.place_main)
                if err:
                    return None, err

                place_common.place_contacts.place_main = place_main
                for place_cuisine_type in place_common.place_cuisine_types:
                    place_cuisine_type.place_main = place_main

                for place_place_type in place_common.place_places_types:
                    place_place_type.place_main = place_main

                for place_service in place_common.place_services:
                    place_service.place_main = place_main

                for place_location in place_common.place_locations:
                    place_location.place_main = place_main

                for place_work_hours_day in place_common.place_work_hours:
                    place_work_hours_day.place_main = place_main

                place_contacts_dao = PlaceContactsDao(conn)
                _, err = await place_contacts_dao.add(place_common.place_contacts)
                if err:
                    return None, err

                place_cuisine_type_dao = PlaceCuisineTypeDao(conn)
                _, err = await place_cuisine_type_dao.add_many(place_common.place_cuisine_types)
                if err:
                    return None, err

                place_place_type_dao = PlacePlaceTypeDao(conn)
                _, err = await place_place_type_dao.add_many(place_common.place_places_types)
                if err:
                    return None, err

                place_service_dao = PlaceServiceDao(conn)
                _, err = await place_service_dao.add_many(place_common.place_services)
                if err:
                    return None, err

                place_location_dao = PlaceLocationDao(conn)
                _, err = await place_location_dao.add_many(place_common.place_locations)
                if err:
                    return None, err

                place_work_hours_dao = PlaceWorkHoursDao(conn)
                _, err = await place_work_hours_dao.add_many(place_common.place_work_hours)
                if err:
                    return None, err

                place_account_role = PlaceAccountRole(
                    place_main=place_common.place_main,
                    account_main=place_common.place_main.account_main,
                    account_status=AccountStatus(id=1)
                )

                place_account_role_dao = PlaceAccountRoleDao(conn)
                _, err = await place_account_role_dao.add(place_account_role)
                if err:
                    return None, err

                menu_main = MenuMain(
                    name=COMMON_MENU_NAME,
                    place_main=place_main,
                    photo=Photo()
                )

                menu_dao = MenuMainDao(conn)
                _, err = await menu_dao.add(menu_main)

                return place_common, None
