def sum_two_smallest_numbers(numbers):
    new_nums = sorted(numbers)
    return new_nums[0] + new_nums[1]




print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))

# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])