#!/usr/bin/env python3
import os

class Containers:
    def __init__(self):
        self.state = {
            1 : ['R', 'P', 'C', 'D', 'B', 'G'],
            2 : ['H', 'V', 'G'],
            3 : ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
            4 : ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
            5 : ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
            6 : ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
            7 : ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
            8 : ['C', 'M', 'D', 'B', 'F'],
            9 : ['F', 'C', 'Q', 'G']
        }

        self.test_state = {
            1 : ['Z', 'N'],
            2 : ['M', 'C', 'D'],
            3 : ['P']
        }


def solve_part1(list_of_commands: list, state: dict) -> str:
    for commands in list_of_commands:
        moves = [int(x) for x in commands.split() if x.isdigit()]

        box_to_move = moves[0]
        source_stack = moves[1]
        target_stack = moves[2]

        while box_to_move > 0:
            state[target_stack].append(state[source_stack].pop())
            box_to_move -= 1

    print(f"final state is {state}")

    out = []
    loop_times = len(state)
    for key in range(1, loop_times+1):
        if len(state[key]) > 0:
            out.append(state[key].pop())

    return "".join(out)



def solve_part2(list_of_commands: list, state: dict) -> str:

    for commands in list_of_commands:
        moves = [int(x) for x in commands.split() if x.isdigit()]

        box_to_move = moves[0]
        source_stack = moves[1]
        target_stack = moves[2]

        source_stack_size = len(state[source_stack])
        boxes_to_be_moved = state[source_stack][source_stack_size-box_to_move:]
        state[target_stack] += boxes_to_be_moved
        del state[source_stack][source_stack_size-box_to_move:]

    print(f"final state is {state}")

    out = []
    loop_times = len(state)
    for key in range(1, loop_times+1):
        if len(state[key]) > 0:
            out.append(state[key].pop())

    return "".join(out)



if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(directory, "input.txt"), encoding="utf-8") as file:
        problem_set = file.read().splitlines()

        c = Containers()
        print(solve_part1(problem_set, c.state))
        c = Containers()
        print(solve_part2(problem_set, c.state))
