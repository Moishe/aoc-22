from collections import deque

f = open('input.txt')
l = f.readline().rstrip()

prev = deque()
for (i, c) in enumerate(l):
    prev.append(c)
    if len(prev) > 14:
        prev.popleft()

        s = set(prev)
        if len(s) == 14:
            print(i + 1, s, prev)
            exit(0)