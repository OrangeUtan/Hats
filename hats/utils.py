from typing import Container


def get_gaps_in_series(start: int, end: int, series: Container[int]):
    return filter(lambda n: n not in series, range(start, end))


def series_as_ranges(nums: list[int]) -> list[tuple[int, int]]:
    """Takes a series of numbers and converts them to a series of ranges.

    A range is represented by a tuple: (start, end).
    """
    ranges = []
    current_range_start = nums[0]
    for prev, current in zip(nums[:-1], nums[1:]):
        if current > prev + 1:
            ranges.append((current_range_start, prev))
            current_range_start = current

    ranges.append((current_range_start, nums[-1]))
    return ranges


def range_to_str(range):
    start, end = range
    if start == end:
        return str(start)
    elif end - start == 1:
        return f"{start}, {end}"
    else:
        return f"{start}..{end}"
