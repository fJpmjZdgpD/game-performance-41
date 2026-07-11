import time
import requests
from requests.exceptions import RequestException

def retry_network_operation(operation, retries=3, delay=1, *args, **kwargs):
    for attempt in range(retries):
        try:
            return operation(*args, **kwargs)
        except RequestException as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e

def fetch_data(url):
    response = retry_network_operation(requests.get, url=url)
    return response.json() if response.status_code == 200 else None
