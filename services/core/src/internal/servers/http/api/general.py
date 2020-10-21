from sanic import Blueprint

from src.internal.servers.http.api.accounts import accounts
from src.internal.servers.http.api.categories import categories
from src.internal.servers.http.api.dishes import dishes
from src.internal.servers.http.api.languages import languages
from src.internal.servers.http.api.measure_unit import measure_units
from src.internal.servers.http.api.menu import menu
from src.internal.servers.http.api.places import places
from src.internal.servers.http.api.cuisine_type import cuisine_types
from src.internal.servers.http.api.currency_type import currency_types
from src.internal.servers.http.api.place_type import place_types
from src.internal.servers.http.api.service import services
from src.internal.servers.http.api.work import work_hours

general_api = Blueprint.group(accounts, places, menu, categories, dishes, languages, cuisine_types, currency_types, place_types, services, work_hours, measure_units, url_prefix='/general')
