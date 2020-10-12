from typing import Any

from sanic import Sanic, Blueprint


class SanicServer:

    _app = Sanic("ined_server_api", load_env=False)

    @classmethod
    def get_app(cls):
        return cls._app

    @classmethod
    def set_main_api(cls, main_api: Blueprint):
        cls._app.blueprint(main_api)

    @classmethod
    def add_cors(cls):
        pass

    @classmethod
    def add_notifiers(cls):
        @cls._app.listener('after_server_start')
        async def notify_server_started(app, loop):
            print('[i] Server successfully started!')

        @cls._app.listener('before_server_stop')
        async def notify_server_stopping(app, loop):
            print('[i] Server shutting down!')

    @classmethod
    def run_server(cls, host: str, port: int, debug: bool, ssl: Any, workers: int, access_log: bool, auto_reload: bool):
        cls._app.run(
            host=host,
            port=port,
            debug=debug,
            ssl=ssl,
            workers=workers,
            access_log=access_log,
            auto_reload=auto_reload
        )
