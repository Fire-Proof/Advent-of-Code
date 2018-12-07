from collections import Counter

with open('input') as input_file:
    data = input_file.read().splitlines()


threes = 0
twos = 0

for row in data:
    count = Counter(row)
    if 3 in count.values():
        threes += 1
    if 2 in count.values():
        twos += 1

print(threes * twos)
