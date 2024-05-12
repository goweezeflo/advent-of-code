"""
--- Day 2: I Was Told There Would Be No Math (Part Two) ---

The elves are also running low on ribbon. Ribbon is all the same width,
so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides,
or the smallest perimeter of any one face.

Each present also requires a bow made out of ribbon as well;
the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.
Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present
plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present
plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

How many total feet of ribbon should they order?
"""

from helper_functions import read_puzzle_input_as_list, logger


def main() -> None:
    perform_tests()
    list_of_dimensions: list[str] = read_puzzle_input_as_list('day-02-input.txt')
    logger.info(day_02_part_2(list_of_dimensions))


def perform_tests() -> None:
    assert day_02_part_2(['2x3x4']) == 34
    assert day_02_part_2(['1x1x10']) == 14


def day_02_part_2(list_of_box_dimensions: list[str], *, sep: str = 'x') -> int:
    total: int = sum([calculate_ribbon_length(box_dimensions, sep=sep) for box_dimensions in list_of_box_dimensions])
    return total


def calculate_ribbon_length(box_dimensions: str, *, sep: str) -> int:
    length, width, height = [int(dimension) for dimension in box_dimensions.split(sep)]
    wrapping_ribbon: int = get_wrapping_ribbon(length, width, height)
    bow: int = get_bow(length, width, height)
    ribbon_length: int = wrapping_ribbon + bow
    logger.debug(f'wrapping_ribbon={wrapping_ribbon}, bow={bow} -> ribbon_length={ribbon_length}')
    return ribbon_length


def get_wrapping_ribbon(length: int, width: int, height: int) -> int:
    """Calculate the perimeter of the smallest side"""
    sorted_dimensions: list[int] = sorted([length, height, width])
    return 2 * (sorted_dimensions[0] + sorted_dimensions[1])


def get_bow(length: int, width: int, height: int) -> int:
    """Calculate ribbon length for the bow by calculating the cubic volume of the box"""
    return length * width * height


if __name__ == '__main__':
    main()
