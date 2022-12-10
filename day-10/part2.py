INPUT = "input.txt"

instructions = [x.split(' ') for x in [x.strip() for x in open(INPUT).readlines()]]

cycle = 0
x = 1
total = 0
scanline = ''

def inccycle():
    global cycle, x, total, scanline
    if cycle % 40 == 0:
        print(scanline)
        scanline = ''
    if (cycle % 40) in [x-1, x, x+1]:
        scanline += '#'
    else:
        scanline += ' '
    cycle += 1

for instruction in instructions:
    inccycle()
    if instruction[0] == 'addx':
        inccycle()
        x += int(instruction[1])

print(scanline)
