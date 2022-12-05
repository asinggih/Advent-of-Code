#!/usr/bin/env python3

import os

def solve_part1(calories_list: str) -> int:

    highest_cal = 0

    current_highest_cal = 0
    for calories in calories_list:
        if calories == "":
            if current_highest_cal > highest_cal:
                highest_cal = current_highest_cal
            current_highest_cal = 0

        else:
            current_highest_cal += int(calories)

    return highest_cal

def solve_part2(calories_list: str) -> int:
    elf_calories = dict()

    current_highest_cal = 0
    for calories in calories_list:
        if calories == "":
            if current_highest_cal not in elf_calories:
                elf_calories[current_highest_cal] = 1
            else:
                elf_calories[current_highest_cal] += 1

            current_highest_cal = 0

        else:
            current_highest_cal += int(calories)

    top_three = []
    for _ in range(3):
        current_max = max(elf_calories)

        elf_calories[current_max] -= 1

        if elf_calories[current_max] == 0:
            elf_calories.pop(current_max)

        top_three.append(current_max)

    return sum(top_three)


if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(directory, "input.txt"), encoding="utf-8") as file:
        problem_list = file.read().splitlines()
        problem_list.append("")
        print(solve_part1(problem_list))
        print(solve_part2(problem_list))
