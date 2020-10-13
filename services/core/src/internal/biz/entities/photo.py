from datetime import datetime
from typing import Optional

from src.configs.internal import BASE_S3_DOMEN
from src.internal.biz.entities.abstract_model import AbstractModel


class Photo(AbstractModel):

    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 full_url: Optional[str] = None,
                 short_url: Optional[str] = None,
                 prefix_name: Optional[str] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__full_url = full_url
        self.__short_url = short_url
        self.__prefix_name = prefix_name

    @property
    def full_url(self):
        return self.__full_url

    @property
    def short_url(self):
        return self.__short_url

    @property
    def prefix_name(self):
        return self.__prefix_name

    def create_full_url(self):
        if not self.__prefix_name:
            self.__prefix_name = BASE_S3_DOMEN
        self.__full_url = self.__prefix_name + self.__short_url
