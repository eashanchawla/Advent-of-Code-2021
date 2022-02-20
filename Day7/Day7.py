import sys
from turtle import position
sys.path.append('..')
from functions import read_file
from typing import Iterable

def preprocess_file(file: Iterable[str]) -> Iterable[int]:
    return list(map(int, file[0].split(',')))


def cost_formula(cost: int) -> int:
    """ Sum of first n natural numbers
    
    Sum = N(N+1) / 2
    """
    return (cost * (cost + 1)) / 2

def simulate_moves(starting_positions: Iterable[int], part: int = 1) -> Iterable[int]:
    """Simulate all possible moves and return the index that leads to least fuel cost"""

    cost_dict = {}
    for index, _ in enumerate(starting_positions):
        position_copy = starting_positions.copy()
        # We remove the position unders consideration from the list copy
        position_copy.pop(index)
        # Find the total fuel cost by subtracting the current position with all the other positions 
        if part == 1:
            position_wise_cost = [abs(positions - starting_positions[index]) for positions in position_copy]
        else:
            position_wise_cost = [abs(positions - starting_positions[index]) for positions in position_copy]
            position_wise_cost = [cost_formula(cost_val) for cost_val in position_wise_cost]

        cost = sum(position_wise_cost)
        cost_dict[starting_positions[index]] = cost
    return min(cost_dict, key=cost_dict.get), cost_dict[min(cost_dict, key=cost_dict.get)]

if __name__ == '__main__':
    # reading and preprocessing input
    file = read_file(sys.argv[1])
    pp_file = preprocess_file(file)
    # part 1 and 2 simulations
    part_1 = simulate_moves(pp_file, part=1)
    part_2 = simulate_moves(pp_file, part=2)

    # print answers
    print(f'Part 1 solution: \n\tBest position: {part_1[0]}\n\tFuel to spend: {part_1[1]}')
    print(f'Part 2 solution: \n\tBest position: {part_2[0]}\n\tFuel to spend: {part_2[1]}')