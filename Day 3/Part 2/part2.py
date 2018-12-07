import re
from itertools import combinations


class Claim(object):
    def __init__(self, _id, from_x, from_y, size_x, size_y):
        self.id = _id
        self.from_x = int(from_x)
        self.from_y = int(from_y)
        self.size_x = int(size_x)
        self.size_y = int(size_y)

    @property
    def to_x(self):
        return self.from_x + self.size_x

    @property
    def to_y(self):
        return self.from_y + self.size_y

    @staticmethod
    def from_string(i):
        data = re.search('#(\d*) @ (\d*),(\d*): (\d*)x(\d*)', i)
        return Claim(*data.groups())

    def __repr__(self) -> str:
        return f'Claim({self.id},{self.from_x},{self.from_y},{self.size_x},{self.size_y})'

    def overlap_area(self, other):
        x1 = max(self.from_x, other.from_x)
        y1 = max(self.from_y, other.from_y)
        x2 = min(self.to_x, other.to_x)
        y2 = min(self.to_y, other.to_y)

        if x1 < x2 and y1 < y2:
            return (x1+x2) * (y1+y2)


def main():
    with open('input') as input_file:
        data = [Claim.from_string(x.strip()) for x in input_file.readlines()]

    for x, y in combinations(data, 2):
        if x.overlap_area(y):
            if x in data:
                data.remove(x)
            if y in data:
                data.remove(y)

    print(data)


if __name__ == '__main__':
    main()
