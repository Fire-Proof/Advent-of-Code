def sum_list(data, offset):
    result = []

    for index, val in enumerate(data):
        try:
            prev = result[index-1]
        except IndexError:
            prev = offset
        result.append(val + prev)

    return result


def main():
    seen = set()
    numbers = [int(x) for x in open('input').readlines()]
    offset = 0
    while True:
        sums = sum_list(numbers, offset)
        for s in sums:
            if s in seen:
                print('Found it: ', s)
                quit(1)
            else:
                seen.add(s)
        offset = sums[-1]


if __name__ == '__main__':
    main()
