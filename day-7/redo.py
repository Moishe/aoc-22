from collections import defaultdict
import re

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000

stack = []
directories = defaultdict(int)

f = open('input.txt')

def cd(dir):
    if dir == '..':
        stack.pop()
    else:
        stack.append(dir)

def size(s):
    for el in stack:
        directories[el] += int(s)

rs = [
    ('^\$ cd (.*)$', cd),
    ('^([0-9]+) .*$', size)
]

for l in f.readlines():
    l = l.rstrip()
    for (idx, r) in enumerate(rs):
        m = re.match(r[0], l)
        if m:
            r[1](m[1])

available = TOTAL_SPACE - directories['/']
need_to_free = NEEDED_SPACE - available

bigger = filter(lambda x: x[1] >= need_to_free, directories.items())
sorted_bigger = sorted(bigger, key=lambda x: x[1])
print(list(sorted_bigger)[0][1])
