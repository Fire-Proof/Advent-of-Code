from itertools import combinations


def diff(x, y):
    result = []
    for a, b in zip(x, y):
        if a == b:
            result.append(a)
    return result


def main():
    with open('input') as input_file:
        data = [x.strip() for x in input_file.readlines()]

    for x, y in combinations(data, 2):
        if len(diff(x, y)) == len(x)-1:
            print("".join(diff(x, y)))


if __name__ == '__main__':
    main()

