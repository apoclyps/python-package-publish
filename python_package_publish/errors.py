from requests.exceptions import JSONDecodeError
from requests.models import HTTPError


class ServiceHTTPError(Exception):
    """Adds response & error_id to base exception"""

    def __init__(self, exception: HTTPError):
        super().__init__(str(exception))
        self.exception = exception
        self.response = exception.response
        self.error_id = None

        if self.response is None:
            return

        # set the error_id if the response has valid json and contains the `error_id`
        try:
            if (json := self.response.json()) and (error_id := json.get("error_id")):
                self.error_id = error_id
        except JSONDecodeError:
            pass

    def __reduce__(self) -> tuple[type, tuple[HTTPError]]:
        return self.__class__, (self.exception,)
