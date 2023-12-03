from collections import defaultdict

# Open, Read, and Strip the input file
with open("./input.txt") as file:
    input_data = file.read().strip()
sum_part1 = 0
sum_part2 = 0

# Iterate over each line in the input data
for line in input_data.split('\n'):
    ok = True
    id_, events = line.split(':')
    V = defaultdict(int)

    # Iterate over each event in the line
    for event in events.split(';'):
        # Iterate over each ball in the event
        for balls in event.split(','):
            n, color = balls.split()
            n = int(n)
            V[color] = max(V[color], n)
            if n > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                ok = False

    # Calculate the score for part 2
    score = 1
    for v in V.values():
        score *= v
    sum_part2 += score

    # Update part 1 sum if 'ok' is True
    if ok:
        sum_part1 += int(id_.split()[-1])

# Print the sums for part 1 and part 2
print(sum_part1)
print(sum_part2)