"""
--- Day 1: Not Quite Lisp ---
--- Part Two ---

Now, given the same instructions, find the position of the first character that causes him to
enter the basement (floor -1). The first character in the instructions has position 1,
the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?
"""

from helper_functions import read_puzzle_input, logger


def change_floor(char: str, floor: int) -> int:
    up: str = '('
    down: str = ')'
    if char == up:
        return floor + 1
    elif char == down:
        return floor - 1
    return floor


def day_01_part_2() -> int:
    puzzle_input: list[str] = read_puzzle_input('01-input.txt')
    instructions: str = puzzle_input[0]
    current_floor: int = 0
    for index, char in enumerate(instructions, start=1):
        current_floor = change_floor(char, current_floor)
        if current_floor < 0:
            return index
    return 0


def main():
    result: int = day_01_part_2()
    logger.info(result)


if __name__ == '__main__':
    main()
