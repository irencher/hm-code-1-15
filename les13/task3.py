# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return
# the result of it. Otherwise, return the result of the second one

from typing import Callable
import random

def choose_func(nums: list[int], func1: Callable, func2: Callable):
    print(nums)
    if all(n > 0 for n in nums):
        print('all nums is positive, selected first func1')
        return func1(nums)
    else:
        print('selected second func2')
        return func2(nums)


def validate_code():
    # Assertions
    for x in range(2):
        nums = [random.randrange(-10, 5 + x + n) for n in range(5)]
        actual_result = choose_func(nums, square_nums, remove_negatives)
        expected_result = (square_nums if all(n > 0 for n in nums) else remove_negatives)(nums)
        assert actual_result == expected_result, f"{actual_result} != {expected_result}"


def square_nums(nums):
    return [num**2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]

validate_code()
