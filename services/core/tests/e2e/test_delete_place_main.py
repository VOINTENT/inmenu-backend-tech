import requests
import json

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.menu_main import MenuMainDao
from src.internal.biz.services.place_service import PlaceService
from tests.test_config import BASE_URL_GENERAL

PLACE_MAIN_ID = 1
PLACE_MAIN_ID_FOR_MISTAKE = 43421


def test_del_place():
    req = requests.delete(f"{BASE_URL_GENERAL}/places/{PLACE_MAIN_ID}")
    assert json.loads(req.text) == {"Status": True}
    assert req.status_code == 200


def test_mistake_menu_main_id():
    menu_main_id, err = MenuMainDao().get_menu_main_id_by_place_main_id(PLACE_MAIN_ID_FOR_MISTAKE)
    assert isinstance(err, Error)
    assert menu_main_id is None
