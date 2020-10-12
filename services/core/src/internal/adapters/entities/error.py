from sanic.response import HTTPResponse, json

from src.internal.adapters.entities.response import Response


class Error(Response):

    def get_response_with_error(self, field=None) -> HTTPResponse:

        msg = self.message

        if field:
            msg += field

        return json({'code': self.code, 'msg': msg}, status=self.status_code)
