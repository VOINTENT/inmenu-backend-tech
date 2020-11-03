from typing import re, Optional

from src.internal.biz.entities.language import Language


def language_serializer(data) -> Optional[Language]:
    try:
        language = Language(
            id=data['language_id'],
            name=data['language_name']
        )
        return language
    except:
        raise TypeError
