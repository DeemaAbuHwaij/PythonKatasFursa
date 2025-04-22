def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return  largest - smallest


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed