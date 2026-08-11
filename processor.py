import numpy as np
def process_game_data(game_data):
    cleaned_data = clean_data(game_data)
    processed_data = perform_analysis(cleaned_data)
    return processed_data

def clean_data(data):
    return [d for d in data if d is not None]

def perform_analysis(data):
    return np.mean(data), np.std(data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, None, 5]
    result = process_game_data(sample_data)
    print(f'Mean: {result[0]}, Std Dev: {result[1]}')