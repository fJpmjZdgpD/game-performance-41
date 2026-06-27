import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError(f'HTTP error occurred: {http_err}') from http_err
        except requests.RequestException as req_err:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError(f'Request exception occurred: {req_err}') from req_err
