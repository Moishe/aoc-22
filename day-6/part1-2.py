from collections import deque

unique_len = 14 # 4 for part 1

f = open('input.txt')
l = f.readline().rstrip()

prev = deque()
for (i, c) in enumerate(l):
    prev.append(c)
    if len(prev) > unique_len:
        prev.popleft()

        s = set(prev)
        if len(s) == unique_len:
            print(i + 1, s, prev)
            exit(0)