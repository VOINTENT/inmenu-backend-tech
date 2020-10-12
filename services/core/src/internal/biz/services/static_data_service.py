from src.internal.biz.services.base_service import BaseService


class StaticDataService(BaseService):

    @staticmethod
    def get_email_code_subject():
        return 'Код подтверждения для inmenu'
