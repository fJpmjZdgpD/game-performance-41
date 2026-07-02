import time
import random

class NetworkError(Exception):
    pass

def retry_operation(func, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return func()
        except NetworkError:
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
            else:
                raise

def mock_network_operation():
    if random.choice([True, False]):
        raise NetworkError('Network failure')
    return 'Success!'

if __name__ == '__main__':
    try:
        result = retry_operation(mock_network_operation)
        print(result)
    except NetworkError as e:
        print(f'Operation failed: {e}')