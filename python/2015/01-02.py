"""
--- Day 1: Not Quite Lisp (Part Two) ---

Now, given the same instructions, find the position of the first character that causes him to
enter the basement (floor -1). The first character in the instructions has position 1,
the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?
"""

from helper_functions import read_puzzle_input_as_string, logger


def main() -> None:
    perform_tests()
    instructions: str = read_puzzle_input_as_string('day-01-input.txt')
    logger.info(day_01_part_2(instructions))


def perform_tests() -> None:
    assert day_01_part_2(')') == 1
    assert day_01_part_2('()())') == 5


def day_01_part_2(instructions: str, current_floor: int = 0) -> int:
    for index, char in enumerate(instructions, start=1):
        current_floor += change_floor(char)
        if current_floor < 0:
            return index
    return 0


def change_floor(char: str) -> int:
    if char == '(':
        return 1  # Move up
    elif char == ')':
        return -1  # Move down
    return 0


if __name__ == '__main__':
    main()
