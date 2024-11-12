"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730677548"


def input_word() -> str:
    """Prompts the user for a 5-character word."""
    user_input = input("Enter a 5-character word:")  # user input
    if len(user_input) == 5:  # Check if the word has 5 characters
        return user_input  # If true, return the word
    else:
        print("Error: Word must contain 5 characters.")  # invalid input notification
        exit()  # returns inputted word


def input_letter() -> str:
    """Prompts the user for a single character."""
    letter_input = input("Enter a single character: ")  # user input
    if len(letter_input) == 1:  # Check if input is one character
        return letter_input  # Return the valid input
    else:
        print("Error: Character must be a single character.")  # Error message
        exit()


def contains_char(word: str, letter: str) -> None:
    """Searches for the letter in the word and prints the result."""
    print(f"Searching for {letter} in {word}")
    match_count = 0  # Initialize match count

    index = 0
    while index < len(word):
        if word[index] == letter:
            print(f"{letter} found at index {index}")
            match_count += 1  # Increment the count if a match is found
        index += 1

    # Output results
    if match_count == 0:
        print(f"No instances of {letter} found in {word}")
    else:
        print(
            f"{match_count} instance{'s' if match_count > 1 else ''} of {letter} found in {word}"
        )


def main() -> None:
    """Main function to run the Chardle exercise."""
    word = input_word()  # Get the word from the user
    letter = input_letter()  # Get the letter guess from the user
    contains_char(word, letter)  # Check if the letter is in the word


if __name__ == "__main__":
    main()
