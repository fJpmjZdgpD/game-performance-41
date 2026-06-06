import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, backoff_factor=0.3):
    tries = 0
    while tries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            tries += 1
            if tries == max_retries:
                raise NetworkError(f'Failed to fetch data from {url}')
            time.sleep(backoff_factor * (2 ** (tries - 1)))
