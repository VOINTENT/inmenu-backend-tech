from sanic import Blueprint
from sanic.request import Request

from src.internal.biz.services.language import LanguageService
from src.internal.servers.http.answers.languages import get_response_get_all_languages
from src.internal.servers.http.middlewares.request import get_lang_id, get_pagination_params

languages = Blueprint('languages', url_prefix='/languages')


@languages.route('', methods=['GET'])
@get_pagination_params
async def get_all_languages(request: Request, pagination_size: int, pagination_after: int):
    languages, err = await LanguageService.get_all_languages(pagination_size, pagination_after)
    if err:
        return err.get_response_with_error()

    return get_response_get_all_languages(languages)
