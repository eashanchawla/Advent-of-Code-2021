from typing import Iterable

import sys
import time


def simulation(starting_state: Iterable[int], days: int = 80) -> int:
    '''Performs a simulation to find the number of lanternfish that will exist at the end of specified time duration '''
    days_completed = 0

    # Creating a list where index indicates the days away from reproduction and value indicates # of fish in that state
    data = [0 for _ in range(9)]
    for value in starting_state:
        data[value] += 1

    # In a loop keep updating states of all lf objects till we hit simulation days. 
    while days_completed < days:
        day_0 = data[0]
        for i in range(1, 9):
            data[i-1] = data[i]
        
        data[6] += day_0
        data[8] = day_0
        days_completed += 1
    
    return sum(data)
             

def read_file(file_name: str) -> Iterable[int]:
    """Read file at location and return a list that represents the starting state"""

    with open(file_name, 'r') as file:
        starting_state = list(map(int, file.read().split(',')))

    return starting_state


if __name__ == '__main__':
    # getting the starting state
    file_to_read = sys.argv[1]
    starting_state = read_file(file_to_read)

    # days is the value passed by the user indicating the # of days for which they want the simulation to be run
    days = int(sys.argv[2])

    # Running the simulation and printing results
    number_of_lf = simulation(starting_state=starting_state, days=days)
    print(f'Number of LanternFishes on day {days}: {number_of_lf}')