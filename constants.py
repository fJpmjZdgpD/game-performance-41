import time

RETRY_LIMIT = 5
RETRY_DELAY = 2

class NetworkError(Exception):
    pass


def retryable_network_operation(func):
    def wrapper(*args, **kwargs):
        for attempt in range(RETRY_LIMIT):
            try:
                return func(*args, **kwargs)
            except NetworkError:
                if attempt < RETRY_LIMIT - 1:
                    time.sleep(RETRY_DELAY)
                else:
                    raise
    return wrapper
