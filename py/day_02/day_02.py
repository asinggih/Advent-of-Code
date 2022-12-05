#!/usr/bin/env python3

import os

values = {
    "A": 1, # A, X = "Rock" # 1
    "X": 1,
    "B": 2, # B, Y = "Paper" # 2
    "Y": 2,
    "C": 3, # C, Z = "Scissors" # 3
    "Z": 3
}

def rps_result(opponent: str, my_choice: str) -> str:

    if (opponent == "A" and my_choice == "Y") or \
        (opponent == "B" and my_choice == "Z") or \
        (opponent == "C" and my_choice == "X"):
        return "w"

    if (opponent == "A" and my_choice == "Z") or \
        (opponent == "B" and my_choice == "X") or \
        (opponent == "C" and my_choice == "Y"):
        return "l"

    else:
        return "d"


def rps_reverse(opponent: str, outc: str) -> str:

    possibilities = ["X", "Y", "Z"]

    if outc == "Y": #draw
        return opponent

    if outc == "Z": #win
        for pos in possibilities:
            if rps_result(opponent, pos) == 'w':
                return pos

    else: # lose
        for pos in possibilities:
            if rps_result(opponent, pos) == 'l':
                return pos



def solve_part1(round_results: list) -> int:

    total_score = 0
    for janken_round in round_results:
        opp, my_choice = janken_round.split()

        choice_val = values[my_choice]

        res = rps_result(opp, my_choice)
        if res == "w":
            match_val = 6
        elif res == "d":
            match_val = 3
        else:
            match_val = 0

        total_score += choice_val + match_val


    return total_score

def solve_part2(round_results: list) -> int:
    # X = lose
    # Y = draw
    # Z = win

    total_score = 0
    for janken_round in round_results:
        opp, outc = janken_round.split()

        if outc == "Z":
            match_val = 6
        elif outc == "Y":
            match_val = 3
        else:
            match_val = 0

        needed_shape = rps_reverse(opp, outc)

        choice_val = values[needed_shape]

        total_score += choice_val + match_val

    return total_score

if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(directory, "input.txt"), encoding="utf-8") as file:
        problem_set = file.read().splitlines()
    print(solve_part1(problem_set))
    print(solve_part2(problem_set))
