import time
import requests

class NetworkRetry:
    def __init__(self, retries=3, backoff=2):
        self.retries = retries
        self.backoff = backoff

    def retry_request(self, func, *args, **kwargs):
        attempt = 0
        while attempt < self.retries:
            try:
                return func(*args, **kwargs)
            except requests.RequestException as e:
                attempt += 1
                if attempt >= self.retries:
                    raise
                time.sleep(self.backoff ** attempt)

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    retrier = NetworkRetry()
    data = retrier.retry_request(fetch_data, 'https://api.example.com/data')
    print(data)