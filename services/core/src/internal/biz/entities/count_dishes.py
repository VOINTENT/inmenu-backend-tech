from typing import Optional


class CountDishes:

    def __init__(self, id: Optional[int] = None
                 , cnt: Optional[int] = None):
        self.__id = id
        self.__cnt = cnt

    @property
    def id(self):
        return self.__id

    @property
    def cnt(self):
        return self.__cnt
