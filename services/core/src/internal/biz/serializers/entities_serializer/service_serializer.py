from typing import re, Optional, List

from src.internal.biz.entities.service import Service


def service_serializer(data: re) -> Optional[List[Service]]:
    try:
        services = [Service(
            id=data[i]['service_id'],
            name=data[i]['service_translate_name']
        ) for i in range(len(data))]
        return services
    except:
        raise TypeError
