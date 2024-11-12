__author__ = "730677548"


def find_and_remove_max(nums: list[int]) -> int:
    if not nums:
        return -1

    max_value = max(nums)
    while max_value in nums:
        nums.remove(max_value)

    return max_value
