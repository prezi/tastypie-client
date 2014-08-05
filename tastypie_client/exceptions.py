"""Exceptions"""


class BaseException(Exception):
    """Base exception for the client"""

    def __init__(self, message=None, **kw):
        super(BaseException, self).__init__(message)
        for key, value in kw.items():
            setattr(self, key, value)


class ApiError(BaseException):
    """Raised by the Client"""


class ResourceTypeMissing(ApiError):
    """Resource type is missing"""


class ResourceIdMissing(ApiError):
    """Resource ID is missing"""


class TooManyResources(ApiError):
    """Too many resources found"""


class HttpError(BaseException):
    """HTTP error"""


class BadHttpStatus(HttpError):
    """Invalid HTTP status"""

    def __init__(self, response):
        message = '%s returned an invalid status code: %s\nLet me vomit the details on you:\n%s' \
                  % (response.url, response.status_code, response.content)
        super(BadHttpStatus, self).__init__(message, response=response)
