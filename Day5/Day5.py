import sys
from typing import List


class LineSegment:
    def __init__(self, line_seg_string: str):
        points = [list(map(int, point.split(',')))
                  for point in line_seg_string.split('->')]
        self._x1, self._y1 = points[0][0], points[0][1]
        self._x2, self._y2 = points[1][0], points[1][1]
        self.covered_points = self.points_covered()

    def calculate_line_equation(self, x, y):
        '''plugs x,y co-ordinate into the line equation of the line segment
        object to return whether it belongs to the line or not.'''
        slope = (self._y2 - self._y1) / (self._x1 - self._x2)
        belongs = True if (y - self._y1) - \
            (slope * (x - self._x1)) == 0 else False
        return belongs

    def points_covered(self):
        '''returns a list of lists of the co-ordinates covered by the line segment object.'''
        if self._x1 == self._x2:
            # this is a vertical line
            if self._y1 < self._y2:
                covered_points = [(self._x1, val)
                                  for val in range(self._y1, self._y2 + 1)]
            else:
                covered_points = [(self._x1, val)
                                  for val in range(self._y2, self._y1 + 1)]
        elif self._y1 == self._y2:
            # this is a horizontal line
            if self._x1 < self._x2:
                covered_points = [(val, self._y1)
                                  for val in range(self._x1, self._x2 + 1)]
            else:
                covered_points = [(val, self._y1)
                                  for val in range(self._x2, self._x1 + 1)]
        else:
            return None
        return covered_points

    def display_covered_points(self):
        '''display the points covered by the line segment object'''
        print('*'*40)
        print('Points covered by the line segment:')
        print(self.covered_points)
        print('*'*40)

    def display_coordinates(self):
        '''display the x and y co-ordinates related to the line segment.'''
        print(f'X1:{self._x1}, Y1:{self._y1}')
        print(f'X2:{self._x2}, Y2:{self._y2}')


def part_1(filename):
    data = open_file(filename)
    linesegments = list()

    # creating an object for each line segment in the dataset that we read
    linesegments = [LineSegment(row) for row in data]

    coords_dict = dict()
    # iterating through the linesegment objects and finding the overlapping coordinates
    for linesegment in linesegments:
        covered_points = linesegment.covered_points
        if covered_points != None:
            for point in covered_points:
                if point not in coords_dict.keys():
                    coords_dict[point] = 1
                else:
                    coords_dict[point] += 1

    required_occurences = [point for point,
                           occurences in coords_dict.items() if occurences >= 2 & occurences is not None]
    print(len(required_occurences))
    pass


def part_2(filename):
    pass


def open_file(filename: str) -> List:
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


if __name__ == '__main__':
    part_1(sys.argv[1])
