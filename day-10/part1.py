INPUT = "input.txt"

instructions = [x.split(' ') for x in [x.strip() for x in open(INPUT).readlines()]]

cycle = 0
x = 1
total = 0

def inccycle():
    global cycle, x, total
    cycle += 1
    if cycle == 20 or (cycle - 20) % 40 == 0:
        total += cycle * x

for instruction in instructions:
    if instruction[0] == 'noop':
        inccycle()
    else:
        for i in range(2): inccycle()
        x += int(instruction[1])

print(total)