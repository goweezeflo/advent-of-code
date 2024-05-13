"""
--- Day 3: Perfectly Spherical Houses in a Vacuum (Part One) ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location,
and then an elf at the North Pole calls him via radio and tells him where to move next.
Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog,
and so his directions are a little off, and Santa ends up visiting some houses more than once.
How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

from helper_functions import read_puzzle_input_as_string, logger


def main() -> None:
    perform_tests()
    all_moves: str = read_puzzle_input_as_string('day-03-input.txt')
    logger.info(day_03_part_1(all_moves))


def perform_tests() -> None:
    assert day_03_part_1('>') == 2
    assert day_03_part_1('^>v<') == 4
    assert day_03_part_1('^v^v^v^v^v') == 2
    # Custom tests
    assert day_03_part_1('') == 1
    assert day_03_part_1('><') == 2
    assert day_03_part_1('>>v<<') == 6
    assert day_03_part_1('>>^^<<v>vv') == 10


def day_03_part_1(all_moves: str) -> int:
    if len(all_moves) == 1:
        return 2
    visited_cells: set[tuple[int, int]] = get_visited_cells(all_moves)
    total_cells_visited: int = len(visited_cells)
    return total_cells_visited


def get_visited_cells(all_moves) -> set[tuple[int, int]]:
    pos_x: int = 0
    pos_y: int = 0
    visited_cells: set[tuple[int, int]] = {(pos_x, pos_y)}  # Register starting position (0, 0)
    logger.debug(f'Position: ({pos_x}, {pos_y})')
    for move in all_moves:
        if move == '>':
            pos_x += 1
        elif move == '<':
            pos_x -= 1
        elif move == '^':
            pos_y += 1
        elif move == 'v':
            pos_y -= 1
        visited_cells.add((pos_x, pos_y))  # Register position (x, y)
        logger.debug(f'Position: ({pos_x}, {pos_y})')
    return visited_cells


if __name__ == "__main__":
    main()
