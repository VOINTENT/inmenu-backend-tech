import os

HOST =              os.environ.get('INMENU_CORE_PG_DB_HOST')
PORT =              int(os.environ.get('INMENU_CORE_PG_DB_PORT'))
USER =              os.environ.get('INMENU_CORE_PG_DB_USER')
PASSWORD =          os.environ.get('INMENU_CORE_PG_DB_PASSWORD')
PRIMARY_DB_NAME =   os.environ.get('INMENU_CORE_PG_PRIMARY_DB_NAME')
LOGS_DB_NAME =      os.environ.get('INMENU_CORE_PG_LOGS_DB_NAME')
