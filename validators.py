def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    return user_input

def main_processing_loop():
    while True:
        user_input = input('Enter command: ')
        try:
            validated_input = validate_input(user_input)
            process_input(validated_input)
        except ValueError as e:
            print(f'Input error: {e}')
            continue

def process_input(validated_input):
    print(f'Processing: {validated_input}')