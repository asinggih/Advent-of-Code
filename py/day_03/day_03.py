#!/usr/bin/env python3
import os

# values = dict()
# for c in range(97, 123):
#     values[chr(c)] = c-96
# for c in range(65, 91):
#     values[chr(c)] = c-38

values = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30,
    'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
    'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50,
    'Y': 51, 'Z': 52
}


def solve_part1(problem_set: list) -> int:

    total = 0
    for rucksack in problem_set:
        midpoint = int(len(rucksack) / 2)
        first_compartment = rucksack[:midpoint]
        second_compartment = set(rucksack[midpoint:])

        inner_join = None
        for item in first_compartment:
            if item in second_compartment:
                inner_join = item
                break

        total += values[inner_join]

    return total


def solve_part2(problem_set: list) -> int:

    window = 3

    total = 0
    for idx in range(0, len(problem_set), window):
        first_group = problem_set[idx]
        second_group = set(problem_set[idx+1])
        third_group = set(problem_set[idx+2])

        inner_join = None
        for item in first_group:
            if item in second_group and item in third_group:
                inner_join = item
                break

        total += values[inner_join]

    return total



if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(directory, "input.txt"), encoding="utf-8") as file:
        rucksacks_combo = file.read().splitlines()

        print(solve_part1(rucksacks_combo))
        print(solve_part2(rucksacks_combo))
