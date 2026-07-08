import time
import requests

class NetworkError(Exception):
    pass

def retry_request(func, retries=3, delay=1, *args, **kwargs):
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except requests.RequestException:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError('Max retries exceeded')

if __name__ == '__main__':
    response = retry_request(requests.get, url='https://api.example.com/data')
    print(response.json())