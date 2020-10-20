from inspect import isawaitable

from sanic.request import Request

from src.internal.adapters.enums.validation_errors import ValidationErrorEnum
from src.internal.biz.dao.language import LanguageDao
from src.internal.servers.http.middlewares.utils import is_digit


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


def get_place_name(func):
    async def wrapper(request: Request, *args, **kwargs):
        place_name = request.args.get('name', '').lower()
        response = func(request, *args, place_name=place_name, **kwargs)
        if isawaitable(response):
            response = await response

        return response
    return wrapper


def get_on_map_params(func):
    async def wrapper(request: Request, *args, **kwargs):
        center_point: str = request.args.get('center_point')
        radius_point: str = request.args.get('radius_point')

        center_point_list = center_point.split(',') if center_point else []
        radius_point_list = radius_point.split(',') if radius_point else []

        if not len(center_point_list) == 2 or not is_digit(center_point_list[0]) or not is_digit(center_point_list[1]):
            center_point_list = None
        else:
            center_point_list[0] = float(center_point_list[0])
            center_point_list[1] = float(center_point_list[1])

        if not len(radius_point_list) == 2 or not is_digit(radius_point_list[0]) or not is_digit(radius_point_list[1]):
            radius_point_list = None
        else:
            radius_point_list[0] = float(radius_point_list[0])
            radius_point_list[1] = float(radius_point_list[1])

        if not center_point_list:
            return ValidationErrorEnum.NOT_FIELD.get_response_with_error('center_point')
        if not radius_point_list:
            return ValidationErrorEnum.NOT_FIELD.get_response_with_error('radius_point')

        response = func(request, *args, center_point_list=center_point_list, radius_point_list=radius_point_list, **kwargs)
        if isawaitable(response):
            response = await response
        return response

    return wrapper
