import logging
from functools import wraps

log = logging.getLogger(__name__)


def exception_handler(log):
    def handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                log.error(str(e), exc_info=True)
                raise e
        return wrapper
    return handler





