from typing import re, Optional, List

from src.internal.biz.entities.service import Service


def service_serializer(data) -> Optional[List[Service]]:
    try:
        return [Service(
            id=data[i]['service_id'],
            name=data[i]['service_translate_name']
        ) for i in range(len(data))]
    except:
        raise TypeError
