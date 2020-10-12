from typing import Optional, List

from src.internal.biz.entities.place_contacts import PlaceContacts
from src.internal.biz.entities.place_cuisine_type import PlaceCuisineType
from src.internal.biz.entities.place_location import PlaceLocation
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.entities.place_place_type import PlacePlaceType
from src.internal.biz.entities.place_service import PlaceService
from src.internal.biz.entities.place_work_hours import PlaceWorkHours


class PlaceCommon:
    def __init__(self,
                 place_main: Optional[PlaceMain] = None,
                 place_contacts: Optional[PlaceContacts] = None,
                 place_cuisine_types: Optional[List[PlaceCuisineType]] = None,
                 place_places_types: Optional[List[PlacePlaceType]] = None,
                 place_services: Optional[List[PlaceService]] = None,
                 place_locations: Optional[List[PlaceLocation]] = None,
                 place_work_hours: Optional[List[PlaceWorkHours]] = None) -> None:
        self.__place_main = place_main
        self.__place_cuisine_types = place_cuisine_types
        self.__place_contacts = place_contacts
        self.__place_places_types = place_places_types
        self.__place_services = place_services
        self.__place_locations = place_locations
        self.__place_work_hours = place_work_hours

    @property
    def place_main(self) -> Optional[PlaceMain]:
        return self.__place_main

    @place_main.setter
    def place_main(self, value: PlaceMain) -> None:
        self.__place_main = value

    @property
    def place_contacts(self) -> Optional[PlaceContacts]:
        return self.__place_contacts

    @property
    def place_cuisine_types(self) -> Optional[List[PlaceCuisineType]]:
        return self.__place_cuisine_types

    @property
    def place_places_types(self) -> Optional[List[PlacePlaceType]]:
        return self.__place_places_types

    @property
    def place_services(self) -> Optional[List[PlaceService]]:
        return self.__place_services

    @property
    def place_locations(self) -> Optional[List[PlaceLocation]]:
        return self.__place_locations

    @property
    def place_work_hours(self) -> Optional[List[PlaceWorkHours]]:
        return self.__place_work_hours
