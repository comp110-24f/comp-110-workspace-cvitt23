__author__: str = "730677548"

"""Dictionary Utility Functions"""


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}

    for key, value in input_dict.items():
        if value in inverted_dict:
            # Raise a KeyError if the value is already a key in inverted_dict
            raise KeyError(f"Duplicate value '{value}'")
        inverted_dict[value] = key  # Invert the key-value pair

    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    if not colors:
        return ""  # Return an empty string if the dictionary is empty

    color_count = {}

    # Count occurrences of each color
    for color in colors.values():
        color_count[color] = color_count.get(color, 0) + 1

    # Determine the most popular color with respect to the order of appearance
    most_popular_color = None
    max_count = 0

    for color in colors.values():
        if color_count[color] > max_count:
            most_popular_color = color
            max_count = color_count[color]

    return most_popular_color  # type: ignore


def count(items: list[str]) -> dict[str, int]:
    counts = {}

    # Loop through each item in the list
    for item in items:
        if item in counts:
            counts[item] += 1  # Increment count if item is already in dictionary
        else:
            counts[item] = 1  # Initialize count to 1 if item is not in dictionary

    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    result = {}

    for word in words:
        # Convert the first letter of the word to lowercase
        first_letter = word[0].lower()

        # If the letter is not already a key in the result, initialize it
        if first_letter not in result:
            result[first_letter] = []

        # Append the word to the list corresponding to its first letter
        result[first_letter].append(word)

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    # Check if the day already exists in the attendance dictionary
    if day not in attendance:
        # If not, initialize it with an empty list
        attendance[day] = []

    # Add the student to the list for the specified day if not already present
    if student not in attendance[day]:
        attendance[day].append(student)

    # Return None (optional, as it does nothing)
    return None
