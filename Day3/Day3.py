import sys
from typing import List


def read_file(filename: str) -> List[List[int]]:
    ''' reads in the text file and converts the file into a list of lists
    '''
    with open(filename, 'r') as file:
        return [list(map(int, val.strip())) for val in file.readlines()]


def bit_conversion(bit_list: List[int]) -> int:
    ''' takes in a sequence of bits and converts it into respective number
    '''
    return sum([2**idx * val for idx, val in enumerate(reversed(bit_list))])


def part_1(data: List[List[int]]) -> int:
    ''' takes in the List of lists and returns the multiplication of the gamma 
        and epsilon rate
    '''
    sum_list = [sum(val) for val in zip(*data)]
    gamma_rate = [1 if val >= len(data) / 2 else 0 for val in sum_list]
    epsilon_rate = [1 if val == 0 else 0 for val in gamma_rate]
    return gamma_rate, epsilon_rate


def filter(rating: List[int], index: int, oxygen_rating: List[int], co2_scrubber_rating: List[int]):
    # Filtering everything on position i

    pass


def part_2(data: List[List[int]]) -> int:
    # gamma is most common, epsilon is least common
    for i in len(data[0]):
        oxygen_rating, co2_scrubber_rating = part_1[data]
        data = filter(data, i, oxygen_rating, co2_scrubber_rating)
    pass


if __name__ == '__main__':
    data = read_file(sys.argv[1])
    print(part_2(data))

    # bit_conversion(gamma_rate) * bit_conversion(epsilon_rate)
