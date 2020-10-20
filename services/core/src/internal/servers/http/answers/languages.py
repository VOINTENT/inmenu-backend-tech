from typing import List

from sanic.response import HTTPResponse, json

from src.internal.biz.entities.language import Language
from src.internal.biz.serializers.language import LanguageSerializer, SER_LANGUAGE_SIMPLE


def get_response_get_all_languages(languages: List[Language]) -> HTTPResponse:
    return json([LanguageSerializer.serialize(language, SER_LANGUAGE_SIMPLE) for language in languages], 200)
