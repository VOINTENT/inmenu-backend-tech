from typing import Any


def check_value(value: Any, *args):
    if not isinstance(value, tuple([type(None), *args])):
        raise TypeError(f'"{value}" has wrong type')
