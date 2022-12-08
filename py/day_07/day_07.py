#!/usr/bin/env python3
import os

def map_all_directories(command_list: list) -> dict():

    dirs = dict()
    stack = [""]

    for command in command_list:

        if command.startswith("$"): # this is a terminal command

            if "ls" in command:
                continue

            if "cd" in command:

                if ".." not in command: # $ cd bla
                    previous_dir = stack[-1]
                    dirname = command.split(" ")[2]
                    current_dir = previous_dir+dirname
                    stack.append(current_dir)

                    if current_dir not in dirs:
                        dirs[current_dir] = 0

                else: # $ cd ..
                    current_dir = stack.pop()


        else: # can be directory or files
            name_combo = command.split(" ")
            if not command.startswith("dir"):
                #only take the number
                name_to_store = int(name_combo[0])
            else:
                name_to_store = 0
            dirs[current_dir] += name_to_store

    completed_dirs = dict()
    for k in dirs:
        current_sum = 0
        for l, v in dirs.items():
            if l.startswith(k):
                current_sum += v
        completed_dirs[k] = current_sum

    return completed_dirs


def solve_part1(command_list: list) -> int:

    dirs_map = map_all_directories(command_list)

    folders_under_threshold = []
    threshold = 100000
    for current_folder_size in dirs_map.values():
        if current_folder_size <= threshold:
            folders_under_threshold.append(current_folder_size)

    return sum(folders_under_threshold)


def solve_part2(command_list: list) -> int:

    dirs_map = map_all_directories(command_list)

    used = dirs_map["/"]
    unused = 70000000-used
    needed = 30000000-unused

    candidates_to_remove = []
    for val in dirs_map.values():
        if val >= needed:
            candidates_to_remove.append(val)

    return min(candidates_to_remove)


if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(directory, "input.txt"), encoding="utf-8") as file:
        problem_set = file.read().splitlines()
        print(solve_part1(problem_set))
        print(solve_part2(problem_set))
