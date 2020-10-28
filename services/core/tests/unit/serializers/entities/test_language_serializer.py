from src.internal.biz.entities.language import Language
from src.internal.biz.serializers.entities_serializer.language_serializer import language_serializer


def test_language_serializer():

    data = {
        'language_id': 1,
        'language_name': 'name',
    }
    language = Language(id=data['language_id'],
                        name=data['language_name'])

    language_1 = language_serializer(data)

    assert isinstance(language, Language)
    assert isinstance(language_1, Language)

    assert language.id == language_1.id
    assert language.name == language_1.name
