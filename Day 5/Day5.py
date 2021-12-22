import sys
from typing import List

class LineSegment:
    def __init__(self, line_seg_string: str):
        points = [list(map(int, point.split(','))) for point in line_seg_string.split('->')]
        self._x1, self._y1 = points[0][0], points[0][1]
        self._x2, self._y2 = points[1][0], points[1][1]

    def points_covered(self):
        '''returns a list of lists of the co-ordinates covered by the line segment object.'''
        pass

    def display_coordinates(self):
        '''display the x and y co-ordinates related to the line segment.'''
        print(f'X1:{self._x1}, Y1:{self._y1}')
        print(f'X2:{self._x2}, Y2:{self._y2}')

def part_1(filename):
    data = open_file(filename)
    linesegments = list()
    
    # creating an object for each line segment in the dataset that we read
    for row in data:
        linesegments.append(LineSegment(row))
    
    # iterating through the linesegment objects and finding the overlapping coordinates
     

    pass

def part_2(filename):
    pass


def open_file(filename: str) -> List:
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


if __name__ == '__main__':
    part_1(sys.argv[1])
