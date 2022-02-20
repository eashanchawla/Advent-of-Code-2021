from typing import Iterable

import sys


class LanternFish():
    def __init__(self, days: int = 8):
        """Initialize an lf object with days_to_child attribute
        
        Days_to_child is based on value passed, or default 8 i.e. creation of a new baby fish. 
        A baby fish will have 8 days to child, as compared to other lf that have 6. 
        """
        self._days_to_child = days

    def update_state(self) -> bool:
        """Function to update state of a lanternfish
        
        If a lantern fish is 0 days away from giving a child, we need to create a new lf object. 
        Else, we simply reduce days to child by 1 day. 
        """
        # if days to child is 0, return true indicating that a new child must be created. Change days to child to 6 
        # else reduce days to child by 1
        if self._days_to_child == 0:
            self._days_to_child = 6
            return True
        else:
            self._days_to_child -= 1
            return False

    def get_days(self) -> int:
        """Return the number of days a fish is away from producing child."""
        return self._days_to_child


def simulation(starting_state: Iterable[int], days: int = 80) -> int:
    '''Performs a simulation to find the number of lanternfish that will exist at the end of specified time duration '''
    days_completed = 0
    current_state = starting_state

    # In a loop keep updating states of all lf objects till we hit 80 simulation days. 
    while days_completed < days:
        current_state_copy = current_state.copy()

        # state updation for each lf in current state
        for lantern_fish in current_state:
            new_lf_needed = lantern_fish.update_state()
            if new_lf_needed:
                current_state_copy.append(LanternFish())
        
        current_state = current_state_copy
        # one simulation day complete
        days_completed += 1
        str_state = str([lf.get_days() for lf in current_state])
    
    if days_completed == days:
        return len(current_state)
             
def convert_to_lf_object(x: int) -> LanternFish:
    """Converts string to LanternFish object"""
    x = int(x)
    return LanternFish(x)


def read_file(file_name: str) -> Iterable[int]:
    """Read file at location and return a list that represents the starting state"""

    with open(file_name, 'r') as file:
        starting_state = list(map(convert_to_lf_object, file.read().split(',')))

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