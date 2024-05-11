"""
--- Day 2: I Was Told There Would Be No Math (Part One) ---

The elves are running low on wrapping paper, and so they need to submit an order for more.
They have a list of the dimensions (length l, width w, and height h) of each present,
and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper
plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper
plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
"""

from helper_functions import read_puzzle_input, logger


def day_02_part_1() -> int:
    list_of_dimensions: list[str] = read_puzzle_input('02-input.txt')
    total = sum([get_wrapping_paper(dimensions) for dimensions in list_of_dimensions])
    return total


def get_wrapping_paper(dimensions: str) -> int:
    length, width, height = [int(dimension) for dimension in dimensions.split('x')]
    box_surface: int = get_box_surface_area(length, width, height)
    smallest_side: int = get_smallest_side_area(length, width, height)
    wrapping_paper: int = box_surface + smallest_side
    logger.debug(f'l-{length}, w-{width}, h-{height} -> {box_surface} + {smallest_side} = {wrapping_paper}')
    return wrapping_paper


def get_box_surface_area(length: int, width: int, height: int) -> int:
    side_1: int = length * width
    side_2: int = width * height
    side_3: int = height * length
    return 2 * (side_1 + side_2 + side_3)


def get_smallest_side_area(length: int, width: int, height: int) -> int:
    sorted_dimensions: list[int] = sorted([length, height, width])
    return sorted_dimensions[0] * sorted_dimensions[1]


if __name__ == '__main__':
    logger.info(day_02_part_1())
