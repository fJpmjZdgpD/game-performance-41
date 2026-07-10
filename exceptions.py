import time
import random

class NetworkError(Exception):
    pass

def retry_on_failure(max_retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except NetworkError:
                    if attempt < max_retries - 1:
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, delay=2)
def fetch_data(url):
    if random.choice([True, False]):
        raise NetworkError('Failed to fetch data')
    return {'data': 'Sample data from ' + url}

if __name__ == '__main__':
    print(fetch_data('http://example.com'))