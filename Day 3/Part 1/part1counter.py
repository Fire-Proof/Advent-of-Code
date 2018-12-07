import re
from collections import Counter
from itertools import product


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


def main():
    with open('input') as input_file:
        data = [Claim.from_string(x.strip()) for x in input_file.readlines()]

    all_fields = []

    for claim in data:
        for x, y in product(range(claim.from_x, claim.to_x), range(claim.from_y, claim.to_y)):
            all_fields.append(f'{x}x{y}')

    counter = Counter(all_fields)
    print(len([x for x, y in counter.items() if y >= 2]))

    print("Final overlap amount")


if __name__ == '__main__':
    main()
