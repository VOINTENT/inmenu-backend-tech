from src.internal.biz.entities.language import Language
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_LANGUAGE_SIMPLE = 'language-simple'


class LanguageSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_LANGUAGE_SIMPLE:
            return cls._serialize_simple
        else:
            raise TypeError

    @staticmethod
    def _serialize_simple(language: Language) -> dict:
        return {
            'id': language.id,
            'name': language.name,
            'code_name': language.code_name
        }
