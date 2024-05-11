import logging
from typing import List

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger("Advent of Code 2015")


def read_puzzle_input(puzzle_input: str) -> list[str]:
    lines: list[str] = []
    try:
        with open(puzzle_input) as input_file:
            for line in input_file:
                lines.append(line.strip())
    except FileNotFoundError:
        logger.error(f'Missing input file: {puzzle_input}')
    return lines
