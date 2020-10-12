from typing import T, Dict, Union

from asyncpg import Record

DES_FROM_DICT = 'des-from-dict'


class BaseDeserializer:
    @classmethod
    def deserialize(cls, obj_dict: Union[Dict, Record], format_ser: str) -> T:
        deserializer = cls._get_deserializer(format_ser)
        return deserializer(obj_dict)

    @classmethod
    def _get_deserializer(cls, format_des: str):
        raise NotImplemented

    @staticmethod
    def _deserializer_from_dict(cls: T):

        def deserializer(obj_dict: dict, cls: T = cls):
            return cls(**obj_dict)

        return deserializer
