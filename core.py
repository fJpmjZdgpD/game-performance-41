import time

def optimize_performance(data):
    start_time = time.perf_counter()
    result = []
    lookup = set(data)

    for item in data:
        if item in lookup:
            result.append(item)

    end_time = time.perf_counter()
    print(f"Processing time: {end_time - start_time:.4f} seconds")
    return result

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 1, 2, 3]
    optimized_result = optimize_performance(sample_data)
    print("Optimized Result:", optimized_result)