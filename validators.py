import json

class Validator:
    @staticmethod
    def validate_non_empty(data):
        if not data:
            raise ValueError('Data cannot be empty.')
        return True

    @staticmethod
    def validate_positive_integer(value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Value must be a positive integer.')
        return True

    @staticmethod
    def validate_json_string(json_string):
        try:
            json.loads(json_string)
        except (ValueError, TypeError):
            raise ValueError('Invalid JSON string.')
        return True

    @staticmethod
    def validate_range(value, min_value, max_value):
        if not (min_value <= value <= max_value):
            raise ValueError(f'Value must be between {min_value} and {max_value}.')
        return True

