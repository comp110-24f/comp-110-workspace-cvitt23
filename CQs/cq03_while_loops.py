"""while loop challenge question """

__author__ = "730677548"


def num_instances(phrase: str, search_char: str) -> int:

    count = 0
    index = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1

    return count
