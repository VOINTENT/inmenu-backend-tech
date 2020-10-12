from src.internal.biz.services.static_data_service import StaticDataService
from src.service.meta.class_property import classproperty


class MailTextsEnum:

    @classproperty
    def SUBJECT_EMAIL_CODE(cls):
        return StaticDataService.get_email_code_subject()
