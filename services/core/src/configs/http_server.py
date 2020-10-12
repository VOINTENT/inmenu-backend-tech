import os

HOST = os.getenv('INMENU_CORE_SERVER_HOST')
PORT = int(os.getenv('INMENU_CORE_SERVER_PORT'))
DEBUG = bool(int(os.getenv('INMENU_CORE_SERVER_DEBUG')))
SSL = None
WORKERS = int(os.getenv('INMENU_CORE_SERVER_WORKERS'))
ACCESS_LOG = bool(int(os.getenv('INMENU_CORE_SERVER_ACCESS_LOG')))
AUTO_RELOAD = bool(int(os.getenv('INMENU_CORE_SERVER_AUTO_RELOAD')))
