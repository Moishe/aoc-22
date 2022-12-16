f = open('/Users/moishelettvin/src/aoc-22/day-14/input.txt')

blocks = {}
DEBUG_BOARD = False


def lineTo(x1, y1, x2, y2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y2, y1) + 1):
            blocks[(x1, y)] = '#'
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            blocks[(x, y1)] = '#'
    else:
        print("Diagonal lines not allowed")
        exit(1)


minx = 499
miny = 1000
maxx = 0
maxy = 0


def draw_board():
    if not DEBUG_BOARD:
        return
    global minx, miny, maxx, maxy
    for y in range(0, maxy + 3):
        line = ''
        for x in range(minx - 1, maxx + 2):
            if y == maxy + 2:
                line += '#'
            elif (x, y) in blocks.keys():
                line += blocks[(x, y)]
            else:
                line += '.'
        print(line)


def clear(pos):
    global blocks
    return pos not in blocks.keys()


def drop_grain():
    global blocks, maxx, minx
    pos = (500, 0)
    while True:
        candidates = [
            (pos[0], pos[1] + 1),
            (pos[0] - 1, pos[1] + 1),
            (pos[0] + 1, pos[1] + 1)
        ]
        for candidate in candidates:
            if clear(candidate):
                pos = candidate
                break
        else:
            blocks[pos] = 'o'
            if pos == (500, 0):
                blocks[pos] = 'o'
                return True
            break

        if pos[1] >= maxy + 1:
            blocks[pos] = 'o'
            break

    maxx = max(pos[0], maxx)
    minx = min(pos[0], minx)
    return False


for l in f.readlines():
    l = l.strip().replace(' ', '')
    coordinates = l.split('->')
    prev = None
    for coordinate in coordinates:
        (x, y) = [int(i) for i in coordinate.split(',')]
        if prev:
            lineTo(prev[0], prev[1], x, y)
        prev = (x, y)
        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(x, maxx)
        maxy = max(y, maxy)

c = 0
draw_board()
while not drop_grain():
    c += 1
    print(c)
    draw_board()
print(c+1)
draw_board()
