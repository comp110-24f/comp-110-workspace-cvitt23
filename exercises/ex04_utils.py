"""list Utility Functions"""

__author__ = "730677548"


def all(lst: list[int], num: int) -> bool:
    if len(lst) == 0:
        return False

    # Iterate through the list
    for element in lst:
        if element != num:
            return False

    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    # Initialize the first element as the maximum
    largest = input[0]

    # finding largest value
    for element in input:
        if element > largest:
            largest = element

    # Return the largest element
    return largest


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    # First, check if the lengths of the lists are different
    if len(lst1) != len(lst2):
        return False

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


def extend(lst1: list[int], lst2: list[int]) -> None:
    for element in lst2:
        # Append each element of lst2 to lst1
        lst1.append(element)
