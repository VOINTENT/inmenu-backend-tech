from src.internal.biz.deserializers.base_deserializer import BaseDeserializer, DES_FROM_DICT
from src.internal.biz.deserializers.cuisine_types import CuisineTypesDeserializer, DES_CUISINE_TYPES_ADD
from src.internal.biz.deserializers.place_contacts import PlaceContactsDeserializer
from src.internal.biz.deserializers.place_locations import PlaceLocationsDeserializer, DES_PLACE_LOCATIONS_ADD
from src.internal.biz.deserializers.place_main import PlaceMainDeserializer, DES_PLACE_MAIN_ADD
from src.internal.biz.deserializers.place_types import PlaceTypesDeserializer, DES_PLACE_TYPES_ADD
from src.internal.biz.deserializers.place_work_hours_week import PlaceWorkHoursWeekDeserializer, DES_WORK_HOURS_WEEK_ADD
from src.internal.biz.deserializers.services import ServicesDeserializer, DES_SERVICES_ADD
from src.internal.biz.entities.place_common import PlaceCommon

DES_PLACE_COMMON_ADD = 'place-common-add'


class PlaceCommonDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_ser: str):
        if format_ser == DES_PLACE_COMMON_ADD:
            return cls._deserializer_add
        else:
            raise TypeError

    @staticmethod
    def _deserializer_add(place_common: dict):
        return PlaceCommon(
            place_main=PlaceMainDeserializer.deserialize(place_common, DES_PLACE_MAIN_ADD),
            place_contacts=PlaceContactsDeserializer.deserialize(place_common['contacts'] if place_common.get('contacts') else {}, DES_FROM_DICT),
            place_cuisine_types=CuisineTypesDeserializer.deserialize(place_common['cuisine_types_ids'] if place_common.get('cuisine_types_ids') else [], DES_CUISINE_TYPES_ADD),
            place_places_types=PlaceTypesDeserializer.deserialize(place_common['place_types_ids'] if place_common.get('place_types_ids') else [], DES_PLACE_TYPES_ADD),
            place_services=ServicesDeserializer.deserialize(place_common['services_ids'] if place_common.get('services_ids') else [], DES_SERVICES_ADD),
            place_locations=PlaceLocationsDeserializer.deserialize(place_common['locations'] if place_common.get('locations') else [], DES_PLACE_LOCATIONS_ADD),
            place_work_hours=PlaceWorkHoursWeekDeserializer.deserialize(place_common['work_hours'] if place_common.get('work_hours') else {}, DES_WORK_HOURS_WEEK_ADD)
        )
