"""wordle new and improved"""

__author__ = "730677548"

WHITE_BOX: str = "⬜"
GREEN_BOX: str = "🟩"
YELLOW_BOX: str = "🟨"


def input_guess(expected_length: int) -> str:
    """Prompt the user to input a guess of the correct length."""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    return char_guess in secret_word


def emojified(guess: str, secret: str) -> str:
    """Compare the guess and secret word, returning a string of emojis."""
    assert len(guess) == len(secret)
    result = ""
    idx = 0

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns = 6
    turn = 0

    while turn < max_turns:
        turn += 1
        print(f"=== Turn {turn}/{max_turns} ===")

        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            print(f"You won in {turn}/{max_turns} turns!")
            return

    print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
