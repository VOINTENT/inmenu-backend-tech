class Response:
    def __init__(self, code: int, message: str, status_code: int) -> None:
        self.code = code
        self.message = message
        self.status_code = status_code
