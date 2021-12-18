import sys
from typing import List

class BingoBoard:
    def __init__(self, row_list: List):
        self._board_elements = [list(map(int, val.split())) for val in row_list]
        self._num_rows = len(self._board_elements)
        self._num_cols = len(self._board_elements[0])
        self._marked_elements = [[1 for _ in range(0,self._num_cols)] for _ in range(0, self._num_rows)]

    def mark_target(self, value: int) -> bool:
        ''' function that marks value passed. 

        Performs the following:
        1. iterating through each element, marking all occurences of variable value passed to the function
        2. calling function bingo check 
        '''
        # marking all occurances. 
        for i in range(0, self._num_rows):
            for j in range(0, self._num_cols):
                if self._board_elements[i][j] == value:
                    # marking ith row, jth column with a 1 i.e. it's been visited / marked on the bingo card
                    self._marked_elements[i][j] = 0
        
        # bingo check 
        if self.bingo_check():
            return True, self.matrix_multiplication() * value
        else:
            return False, 0

    def bingo_check(self) -> bool:
        ''' function to check whether bingo was reached or not'''
        # calculating row and column sums of bingo board marked elements
        column_sum = list(map(sum, zip(*self._marked_elements)))
        row_sum = [sum(row_list) for row_list in self._marked_elements]

        # check to see if bingo was achieved
        return True if (0 in column_sum or 0 in row_sum) else False

    def matrix_multiplication(self):
        ''' function to perform matrix multiplication on board_elements and marked_elements list of lists.'''
        mat_mult = [[x * y for x, y in zip(i,v)] for i,v in zip(self._board_elements, self._marked_elements)]
        return sum([sum(val) for val in mat_mult])


    def get_board(self) -> List[List[int]]:
        return self._board_elements


def open_file(filename: str, chunk_size: int):
    with open(filename, 'r') as file:
        # reading in the file
        data = file.readlines()
        number_selections = list(map(int, data[0].split(',')))

        # keeping a count of the elements read and the number of boards
        board_objects = list()

        # iterating chunk_size rows at a time and creating bingo_board objects in each iteration
        board_objects = [
                        BingoBoard(data[i:]) if 
                                                (i + chunk_size) > len(data) 
                                            else 
                        BingoBoard(data[i:i+chunk_size-1]) 
                                            for i in range(2, len(data), chunk_size)
                        ]
    
    return number_selections, board_objects

def part_1(filename: str, chunk_size: int):
    # opening file 
    number_selections, board_objects = open_file(filename, chunk_size)
    # checking board objects
    for number in number_selections:
        for board in board_objects:
            bingo_check, answer = board.mark_target(number)
            if bingo_check:
                print('-'*40)
                print('Part 1 answer:', answer)
                print('-'*40)
                break
        if bingo_check:
            break
    return None

def part_2(filename: str, chunk_size: int) -> int:
    # opening file 
    number_selections, board_objects = open_file(filename, chunk_size)
    # checking board objects
    bingo_answers = list()
    for number in number_selections:
        for index, board in enumerate(board_objects):
            bingo_check, answer = board.mark_target(number)
            if bingo_check:
                bingo_answers.append(answer)
                break
        
        if bingo_check:
            board_objects.remove(board)

    print('-'*40)
    print('Part 2 answer:', bingo_answers[-1])
    print('-'*40)

    return None


if __name__ == '__main__':
    part_1(sys.argv[1], 6)
    part_2(sys.argv[1], 6)