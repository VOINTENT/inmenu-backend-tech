from sanic import Blueprint

from src.internal.servers.http.api.accounts import accounts
from src.internal.servers.http.api.categories import categories
from src.internal.servers.http.api.dishes import dishes
from src.internal.servers.http.api.languages import languages
from src.internal.servers.http.api.menu import menu
from src.internal.servers.http.api.places import places

general_api = Blueprint.group(accounts, places, menu, categories, dishes, languages, url_prefix='/general')
