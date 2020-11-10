from typing import Tuple, Optional, List

from loguru import logger

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.dao.menu_category import MenuCategoryDao
from src.internal.biz.dao.menu_main import MenuMainDao
from src.internal.biz.dao.place_account_role import PlaceAccountRoleDao
from src.internal.biz.dao.place_contacts import PlaceContactsDao
from src.internal.biz.dao.place_cuisine_type_dao import PlaceCuisineTypeDao
from src.internal.biz.dao.place_location import PlaceLocationDao
from src.internal.biz.dao.place_main_dao import PlaceMainDao
from src.internal.biz.dao.place_place_type import PlacePlaceTypeDao
from src.internal.biz.dao.place_service_dao import PlaceServiceDao
from src.internal.biz.dao.place_work_hours import PlaceWorkHoursDao
from src.internal.biz.deserializers.photo import PHOTO_SHORT_URL
from src.internal.biz.deserializers.place_common import PLACE_COMMON, PlaceCommonDeserializer, \
    DES_PLACE_COMMON_FROM_DB_FULL
from src.internal.biz.deserializers.place_contacts import PLACE_CONTACTS, PLACE_CONTACTS_EMAIL, \
    PLACE_CONTACTS_SITE_LINK, PLACE_CONTACTS_VK_LINK, PLACE_CONTACTS_INSTAGRAM_LINK, PLACE_CONTACTS_FACEBOOK_LINK, \
    PLACE_CONTACTS_PHONE_NUMBER
from src.internal.biz.deserializers.place_location import PLACE_LOCATION_FULL_ADDRESS, PLACE_LOCATION, PLACE_LOCATION_ID
from src.internal.biz.deserializers.place_main import PLACE_MAIN_ID, PLACE_MAIN_NAME, PLACE_MAIN, TEMP_GET_NULL_INT, \
    TEMP_GET_NULL_STR
from src.internal.biz.entities.account_status import AccountStatus
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_account_role import PlaceAccountRole
from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.entities.place_main import PlaceMain

COMMON_MENU_NAME = 'Основное'
COMMON_CATEGORY_NAME = 'Первые блюда'


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

                menu_category = MenuCategory(
                    menu_main=menu_main,
                    name=COMMON_CATEGORY_NAME
                )

                _, err = await MenuCategoryDao(conn).add(menu_category)
                if err:
                    return None, err

                return place_common, None

    async def get_by_location_id(self, place_location_id: int) -> Tuple[Optional[PlaceCommon], Optional[Error]]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(f"""
                SELECT
                    place_location.full_location    AS {PLACE_COMMON + PLACE_LOCATION_FULL_ADDRESS},
                    place_location.id               AS {PLACE_COMMON + PLACE_LOCATION_ID},
                    place_main.name                 AS {PLACE_COMMON + PLACE_MAIN_NAME},
                    place_main.photo_link           AS {PLACE_COMMON + PLACE_MAIN + PHOTO_SHORT_URL},
                    place_main.id                   AS {PLACE_COMMON + PLACE_MAIN_ID},
                    place_contacts.phone_number     AS {PLACE_COMMON + PLACE_CONTACTS_PHONE_NUMBER},
                    place_contacts.email            AS {PLACE_COMMON + PLACE_CONTACTS_EMAIL},
                    place_contacts.site_link        AS {PLACE_COMMON + PLACE_CONTACTS_SITE_LINK},
                    place_contacts.vk_link          AS {PLACE_COMMON + PLACE_CONTACTS_VK_LINK},
                    place_contacts.instagram_link   AS {PLACE_COMMON + PLACE_CONTACTS_INSTAGRAM_LINK},
                    place_contacts.facebook_link    AS {PLACE_COMMON + PLACE_CONTACTS_FACEBOOK_LINK}
                FROM
                    place_location
                    INNER JOIN place_main ON place_location.place_main_id = place_main.id
                    INNER JOIN place_contacts ON place_contacts.place_main_id = place_main.id
                WHERE
                    place_location.id = $1
            """, place_location_id)

            if not row:
                return None, None

            return PlaceCommonDeserializer.deserialize(row, DES_PLACE_COMMON_FROM_DB_FULL), None

    async def update(self, place_main_id: int, place_common: PlaceCommon) -> Tuple[Optional[PlaceCommon], Optional[Error]]:
        async with self.pool.acquire() as conn:
            async with conn.transaction():

                place_main_dao = PlaceMainDao(conn)
                place_main, err = await place_main_dao.update(place_main_id, place_common.place_main)
                if err:
                    return None, err

                if place_common.place_places_types:
                    for place_place_type in place_common.place_places_types:
                        place_place_type.place_main = place_main

                    place_place_type_dao = PlacePlaceTypeDao(conn)
                    if place_common.place_places_types[0].place_type.id == TEMP_GET_NULL_INT:
                        _, err = await place_place_type_dao.delete(place_main_id)
                        if err:
                            return None, err
                    else:
                        _, err = await place_place_type_dao.delete(place_common.place_places_types[0].place_main.id)
                        if err:
                            return None, err

                        _, err = await place_place_type_dao.add_many(place_common.place_places_types)
                        if err:
                            return None, err

                if place_common.place_services:
                    for place_service in place_common.place_services:
                        place_service.place_main = place_main
                    place_service_dao = PlaceServiceDao(conn)
                    if place_common.place_services[0].service.id == TEMP_GET_NULL_INT:
                        _, err = await place_service_dao.delete(place_common.place_services[0].place_main.id)
                        if err:
                            return None, err
                    else:
                        _, err = await place_service_dao.delete(place_common.place_services[0].place_main.id)
                        if err:
                            return None, err

                        _, err = await place_service_dao.add_many(place_common.place_services)
                        if err:
                            return None, err

                if place_common.place_cuisine_types:
                    for place_cuisine_type in place_common.place_cuisine_types:
                        place_cuisine_type.place_main = place_main

                    place_cuisine_type_dao = PlaceCuisineTypeDao(conn)

                    if place_common.place_cuisine_types[0].cuisine_type.id == TEMP_GET_NULL_INT:
                        _, err = await place_cuisine_type_dao.delete(place_common.place_cuisine_types[0].place_main.id)
                        if err:
                            return None, err
                    else:
                        _, err = await place_cuisine_type_dao.delete(place_common.place_cuisine_types[0].place_main.id)
                        if err:
                            return None, err
                        _, err = await place_cuisine_type_dao.add_many(place_common.place_cuisine_types)
                        if err:
                            return None, err

                if place_common.place_work_hours:
                    for place_work_hours_day in place_common.place_work_hours:
                        place_work_hours_day.place_main = place_main
                    place_work_hours_dao = PlaceWorkHoursDao(conn)
                    if place_common.place_work_hours[0].id == TEMP_GET_NULL_INT:
                        _, err = await place_work_hours_dao.delete(place_common.place_work_hours[0].place_main.id)
                        if err:
                            return None, err
                    else:
                        _, err = await place_work_hours_dao.delete(place_common.place_work_hours[0].place_main.id)
                        if err:
                            return None, err
                        _, err = await place_work_hours_dao.add_many(place_common.place_work_hours)
                        if err:
                            return None, err

                if place_common.place_location:
                    place_common.place_location.place_main = place_main
                    place_location_dao = PlaceLocationDao(conn)
                    if place_common.place_location.id == TEMP_GET_NULL_INT:
                        _, err = await place_location_dao.delete(place_common.place_location.place_main.id)
                        if err:
                            return None, err
                    else:
                        _, err = await place_location_dao.delete(place_common.place_location.place_main.id)
                        if err:
                            return None, err
                        _, err = await place_location_dao.add_many(place_locations=[place_common.place_location])
                        if err:
                            return None, err

                if place_common.place_contacts:
                    place_common.place_contacts.place_main = place_main
                    place_contacts_dao = PlaceContactsDao(conn)
                    if place_common.place_contacts.id == TEMP_GET_NULL_INT:
                        _, err = await place_contacts_dao.delete(place_common.place_contacts.place_main.id)
                        if err:
                            return None, err
                    else:
                        _, err = await place_contacts_dao.update(place_common.place_contacts.place_main.id, place_common.place_contacts)
                        if err:
                            return None, err

                return place_common, None
