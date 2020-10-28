from typing import re, Optional, List

from src.internal.biz.entities.service import Service


def service_serializer(dictionary: dict) -> Optional[Service]:
    try:
        return Service(
            id=dictionary['service_id'],
            name=dictionary['service_name']
        )
    except:
        raise TypeError
