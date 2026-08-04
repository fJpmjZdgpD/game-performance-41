def divide_numbers(numerator, denominator):
    if denominator == 0:
        raise ValueError('Denominator cannot be zero.')
    return numerator / denominator

def safely_divide(numerator, denominator):
    try:
        return divide_numbers(numerator, denominator)
    except ValueError as e:
        return str(e)

def get_item_from_list(item_list, index):
    try:
        return item_list[index]
    except IndexError:
        return 'Index out of range'

def parse_integer(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 'Invalid integer value'

def main():
    print(safely_divide(10, 0))  # Example of handling division by zero
    print(get_item_from_list([1, 2, 3], 5))  # Example of handling index error
    print(parse_integer('abc'))  # Example of handling invalid integer

if __name__ == '__main__':
    main()