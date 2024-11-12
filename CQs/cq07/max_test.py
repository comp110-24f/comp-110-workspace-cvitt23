__author__ = "730677548"

import unittest
from find_max import find_and_remove_max


class TestFindAndRemoveMax(unittest.TestCase):

    def test_return_value(self) -> None:
        """Test that the correct maximum value is returned"""
        lst = [10, 9, 8, 7, 10]
        result = find_and_remove_max(lst)
        self.assertEqual(result, 10)

    def test_mutation_of_list(self) -> None:
        """Test that the input list is mutated correctly after max removal"""
        lst = [10, 9, 8, 7, 10]
        find_and_remove_max(lst)
        self.assertEqual(lst, [9, 8, 7])

    def test_empty_list(self) -> None:
        """Test edge case of empty list, should return -1 and leave list unchanged"""
        lst = []
        result = find_and_remove_max(lst)
        self.assertEqual(result, -1)
        self.assertEqual(lst, [])  # Ensure the list is not mutated

    def test_all_max_values(self) -> None:
        """Test edge case where all values are the same and the max value"""
        lst = [5, 5, 5, 5]
        result = find_and_remove_max(lst)
        self.assertEqual(result, 5)
        self.assertEqual(lst, [])  # After removal, the list should be empty


if __name__ == "__main__":
    unittest.main()
