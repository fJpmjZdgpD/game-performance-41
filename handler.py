import requests
import time

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError('Network request failed after retries')

# Example usage
def fetch_data(url):
    try:
        return retry_request(url)
    except NetworkError as e:
        print(e)  # Handle the error as appropriate
