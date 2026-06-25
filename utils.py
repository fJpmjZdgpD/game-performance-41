import time
import random

class NetworkError(Exception):
    pass

def retry(func, retries=3, delay=1):
    for attempt in range(retries):
        try:
            return func()
        except NetworkError:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise

def network_operation():
    if random.choice([True, False]):
        raise NetworkError('Simulated network failure')
    return 'Network operation successful'

if __name__ == '__main__':
    try:
        result = retry(network_operation)
        print(result)
    except NetworkError as e:
        print(f'Operation failed after retries: {e}')