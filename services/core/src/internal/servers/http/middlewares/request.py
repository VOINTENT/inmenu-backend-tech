from inspect import isawaitable

from sanic.request import Request

from src.internal.biz.dao.language import LanguageDao


def get_pagination_params(func):
    async def wrapper(request: Request, *args, **kwargs):
        pagination_size = request.args.get('pagination_size')
        pagination_after = request.args.get('pagination_after')

        if not pagination_size or not pagination_size.isdigit() or int(pagination_size) > 100:
            pagination_size = 100
        else:
            pagination_size = int(pagination_size)

        if not pagination_after or not pagination_after.isdigit():
            pagination_after = 0
        else:
            pagination_after = int(pagination_after)

        response = func(request, *args, pagination_size=pagination_size, pagination_after=pagination_after, **kwargs)
        if isawaitable(response):
            response = await response
        return response

    return wrapper


def get_city_name(func):
    async def wrapper(request: Request, *args, **kwargs):
        city_name = request.args.get('city')
        response = func(request, *args, city_name=city_name, **kwargs)
        if isawaitable(response):
            response = await response
        return response
    return wrapper


def get_lang_id(func):
    async def wrapper(request: Request, *args, **kwargs):
        lang_code_name = request.headers.get('lang')
        lang_id = 1
        if lang_code_name:
            lang, err = await LanguageDao().get_id_by_code_name(lang_code_name)
            if lang:
                lang_id = lang.id

        response = func(request, *args, lang_id=lang_id, **kwargs)
        if isawaitable(response):
            response = await response

        return response
    return wrapper