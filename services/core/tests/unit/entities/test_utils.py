import pytest

from src.internal.biz.entities.utils import check_value


def test_check_value():

    check_value(None, str, int, float)
    check_value('123', str)
    check_value(123, int)
    check_value(123.0, float)
    check_value(True, bool)

    with pytest.raises(TypeError):
        check_value(123, str)

    with pytest.raises(TypeError):
        check_value('123', int)
