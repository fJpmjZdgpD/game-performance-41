import requests
import time

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=5, backoff_factor=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise NetworkError(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException:
            retries += 1
            time.sleep(backoff_factor * (2 ** retries))
    raise NetworkError(f'Max retries reached for {url}')
