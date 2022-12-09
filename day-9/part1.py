import numpy as np

f = open('input.txt')

dxdy = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1),
    'LU': (-1, -1),
    'RU': (1, -1),
    'LD': (-1, 1),
    'RD': (1, 1)
}

visited = set()

def move_tail(tail, head):
    if not np.array_equal(tail, head):
        dist = head - tail
        absdist = np.array([abs(x) for x in dist])
        if np.array_equal(absdist, [0,2]) or np.array_equal(absdist, [2,0]):
            tail += np.array([int(x/2) for x in dist])
        else:
            if max(absdist) == 2:
                norm = [int(x) for x in dist / absdist]
                tail += norm

    visited.add((tail[0], tail[1]))
    return tail

head = np.array([0,0])
tail = np.array([0,0])
commands = [l.strip().split(' ') for l in f.readlines()]
for (direction, distance) in [(x[0], int(x[1])) for x in commands]:
    (dx,dy) = dxdy[direction]
    for step in range(distance):
        head += dxdy[direction]
        tail = move_tail(tail, head)
        print(direction, distance, step, head, tail)

print(len(list(visited)))