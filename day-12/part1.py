from collections import deque
import math
import numpy as np

grid = np.array([[c for c in l.strip()]
                for l in open('input.txt').readlines()], ndmin=2)
visited = set()

# find the start position
starts = []
for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        if grid[y, x] == 'S' or grid[y, x] == 'a':
            starts.append((y, x))
            grid[y, x] = 'a'
        elif grid[y, x] == 'E':
            end = (y, x)
            grid[y, x] = 'z'

paths = deque([(start, []) for start in starts])


def maybeEnqueue(pos, path):
    global visited
    if pos[0] >= 0 and pos[0] < grid.shape[0] and pos[1] >= 0 and pos[1] < grid.shape[1]:
        if pos not in path and pos not in visited:
            last = path[-1]
            diff = ord(grid[pos]) - ord(grid[last])
            if diff <= 1:
                paths.append((pos, path))
                visited.add(pos)


def h(x):
    global end
    (pos, path) = x
    dy = pos[0] - end[0]
    dx = pos[1] - end[1]
    v = len(path) * 100 - (ord(grid[pos]) -
                           ord('a')) - math.sqrt(dx * dx + dy * dy)
    print(pos, grid[pos], end, v)
    return v


def sortQueue():
    global paths
    paths = deque(sorted(paths, key=lambda x: h(x)))


while len(paths):
    (pos, path) = paths.popleft()
    if pos == end:
        print("Found in %d steps" % len(path))
        exit(0)
    new_path = path.copy()
    new_path.append(pos)
    maybeEnqueue((pos[0] - 1, pos[1]), new_path)
    maybeEnqueue((pos[0] + 1, pos[1]), new_path)
    maybeEnqueue((pos[0], pos[1] - 1), new_path)
    maybeEnqueue((pos[0], pos[1] + 1), new_path)
    # sortQueue()

print("not found")
exit(1)
