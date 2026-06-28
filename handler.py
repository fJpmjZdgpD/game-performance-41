import time
import requests
from requests.exceptions import RequestException

def retry_request(url, retries=3, backoff=1):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException:
            if attempt < retries - 1:
                time.sleep(backoff * (2 ** attempt))
            else:
                raise

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except RequestException as e:
        print(f'Network request failed: {e}')