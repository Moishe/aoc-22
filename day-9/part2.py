import numpy as np

f = open('input.txt')

dxdy = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1),
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

    return tail

def print_board(segments):
    for y in range(-5, 5):
        row = ''
        for x in range(-5, 5):
            found_segment = False
            for (idx, segment) in enumerate(segments):
                if np.array_equal(segment, [x,y]):
                    row += str(idx)
                    found_segment = True
                    break
            if not found_segment:
                row += '.'
        print(row)
    print()


LENGTH = 10 # use length 2 for part 1
segments = [np.array([0,0]) for i in range(LENGTH)]
commands = [l.strip().split(' ') for l in f.readlines()]
for (direction, distance) in [(x[0], int(x[1])) for x in commands]:
    (dx,dy) = dxdy[direction]
    for step in range(distance):
        segments[0] += dxdy[direction]
        for segmentidx in range(len(segments) - 1):
            nextsegment = segmentidx + 1
            segments[nextsegment] = move_tail(segments[nextsegment], segments[segmentidx])
        tail = segments[-1]
        visited.add((tail[0], tail[1]))
        #print_board(segments)

print(len(list(visited)))