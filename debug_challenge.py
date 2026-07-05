def find_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    count = len(numbers)
    for num in numbers:
        total += num
    return total / count


def find_max_difference(numbers):
    """Find the maximum difference between any two numbers in the list."""
    max_diff = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff


def count_above_average(numbers):
    """Count how many numbers are above the average."""
    avg = find_average(numbers)
    count = 0
    for num in numbers:
        if num > avg:
            count += 1
    return count


if __name__ == "__main__":
    test_data = [10, 20, 30, 40, 50]

    print(f"Average: {find_average(test_data)}")
    print(f"Max difference: {find_max_difference(test_data)}")
    print(f"Above average: {count_above_average(test_data)}")
