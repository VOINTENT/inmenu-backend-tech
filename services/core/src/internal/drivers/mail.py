import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from src.configs.mail import HOST, PORT, FROM
from src.internal.adapters.enums.mail_texts import MailTextsEnum

EMAIL_CODE_TYPE = 'email-code-type'
EMAIL_CODE_CONTENT_TYPE = 'plain'


class Mail:

    @classmethod
    def send_email(cls, message_type: str, address: str, message: str) -> bool:
        sender = cls._get_sender(message_type)
        return sender(address, message)

    @classmethod
    def _get_sender(cls, message_type: str):
        if message_type == EMAIL_CODE_TYPE:
            return cls._email_code_sender
        else:
            raise TypeError

    @staticmethod
    def _email_code_sender(address: str, message: str) -> bool:
        msg = MIMEMultipart()

        msg['From'] = FROM
        msg['To'] = address
        msg['Subject'] = MailTextsEnum.SUBJECT_EMAIL_CODE

        msg.attach(MIMEText(message, EMAIL_CODE_CONTENT_TYPE))

        try:
            server = smtplib.SMTP(f'{HOST}: {PORT}')
        except:
            print('[x] Connection to mail server refused')
            return False

        try:
            server.starttls()
        except:
            print('[x] TLS connectiona failed!')
            return False

        try:
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        except Exception as exc:
            print('[x] Unsuccessfully sent email to %s' % msg['To'])
            print(traceback.format_exc())
            return False
        else:
            print('[i] Successfully sent email to %s' % msg['To'])
            return True
        finally:
            server.quit()
