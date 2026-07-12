import time

def measure_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Execution time of {func.__name__}: {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@measure_performance
def process_game_data(data):
    result = []
    for item in data:
        # Optimized processing logic
        result.append(item * 2)  # Example operation
    return result

@measure_performance
def load_game_assets(assets):
    loaded_assets = []
    for asset in assets:
        loaded_assets.append(load_asset(asset))
    return loaded_assets

def load_asset(asset):
    time.sleep(0.1)  # Simulates asset loading
    return asset
