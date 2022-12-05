#!/usr/bin/env python3
import os

def solve_part1(list_of_pairs: list) -> int:

    overlap = 0
    for pairs in list_of_pairs:
        elf_one, elf_two = pairs.split(",")

        elf_one_min, elf_one_max = elf_one.split("-")
        elf_two_min, elf_two_max = elf_two.split("-")

        if ((int(elf_one_min) <= int(elf_two_min)) and (int(elf_one_max) >= int(elf_two_max))) or \
            ((int(elf_two_min) <= int(elf_one_min)) and (int(elf_two_max) >= int(elf_one_max))):
            overlap += 1

    return overlap

def solve_part2(list_of_pairs: list) -> int:

    overlap = 0
    for pairs in list_of_pairs:
        elf_one, elf_two = pairs.split(",")

        elf_one_min, elf_one_max = elf_one.split("-")
        elf_two_min, elf_two_max = elf_two.split("-")

        elf_one_items = set(list(range(int(elf_one_min), int(elf_one_max)+1)))
        elf_two_items = set(list(range(int(elf_two_min), int(elf_two_max)+1)))

        overlaps_exist = len(elf_one_items.intersection(elf_two_items)) > 0
        if overlaps_exist:
            overlap += 1

    return overlap




if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(directory, "input.txt"), encoding="utf-8") as file:
        problem_set = file.read().splitlines()

        print(solve_part1(problem_set))
        print(solve_part2(problem_set))
        # print(solve_part2(problem_set))
