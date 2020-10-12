from typing import Optional

from src.configs.internal import BASE_S3_DOMEN


class Photo:

    def __init__(self,
                 full_url: Optional[str] = None,
                 short_url: Optional[str] = None,
                 prefix_name: Optional[str] = None) -> None:
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
