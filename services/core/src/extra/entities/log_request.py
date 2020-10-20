class LogRequest:

    def __init__(self, completion_time: float = None, method: str = None, url: str = None, ip: str = None,
                 status: int = None, error_msg: int = None) -> None:
        self.completion_time = completion_time
        self.method = method
        self.url = url
        self.ip = ip
        self.status = status
        self.error_msg = error_msg
