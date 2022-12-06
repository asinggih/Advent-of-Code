#!/usr/bin/env python3
import os

from collections import deque

def marker_detector(datastream: list, window: int) -> int:

    marker_container = deque()
    for idx, char in enumerate(datastream):
        if len(marker_container) == window:
            deduped = set(marker_container)
            if len(deduped) == window:
                return idx
            marker_container.popleft()
        marker_container.append(char)
    return -1


def solve_part1(datastream: list) -> int:

    return marker_detector(datastream, 4)


def solve_part2(datastream: list) -> int:

    return marker_detector(datastream, 14)



if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(directory, "input.txt"), encoding="utf-8") as file:
        problem_set = file.read()

        print(solve_part1(problem_set))
        print(solve_part2(problem_set))
