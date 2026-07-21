import time
import requests

class NetworkRetryError(Exception):
    pass

def retry_request(url, max_retries=3, backoff_factor=0.3):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException:
            attempt += 1
            if attempt == max_retries:
                raise NetworkRetryError(f'Failed to retrieve data from {url} after {max_retries} attempts')
            time.sleep(backoff_factor * (2 ** attempt))