import json
import re
from collections import Counter
from pprint import pprint

guards = {}


def main():
    with open('input') as input_file:
        lines = [x.strip() for x in input_file.readlines()]

    current_guard = None
    fell_asleep = None
    for line in lines:
        if 'Guard' in line:
            current_guard = int(re.search('Guard #(\d*) begins shift', line).group(1))
        if 'falls asleep' in line:
            fell_asleep = int(re.search('\[\d*-\d*-\d* 00:(\d*)\]', line).group(1))
        if 'wakes up' in line:
            woke = int(re.search('\[\d*-\d*-\d* 00:(\d*)\]', line).group(1))
            if current_guard in guards.keys():
                    guards[current_guard].extend(range(fell_asleep, woke))
            else:
                guards[current_guard] = list(range(fell_asleep, woke))

    result = {key: {
        'max_minute': Counter(val).most_common(1)[0][0],
        'max_amount': Counter(val).most_common(1)[0][1],
        'sum': len(val)
    } for key, val in guards.items()}

    sort = sorted(result.items(), key=lambda x: x[1]['max_amount'], reverse=True)
    print(sort[0][0] * sort[0][1]['max_minute'])


if __name__ == '__main__':
    main()
