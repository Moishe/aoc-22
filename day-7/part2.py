import json
import re

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000

f = open('input.txt')

def cd(m, tree, path):
    if (m[1]) == '..':
        path.pop()
    else:
        path.append(m[1])
    n = tree
    for e in path:
        if e not in n:
            n[e] = {}
        n = n[e]

    return (tree, path)

def size(m, tree, path):
    n = tree
    for e in path:
        if e not in n:
            n[e] = {}
        n = n[e]
    n[m[2]] = int(m[1])
    return (tree, path)

def get_total_size(name, node, all_sizes):
    size_node = {}
    total_size = 0
    for (k, v) in node.items():
        if type(v) == dict:
            total_size += get_total_size(k, v, all_sizes)
        else:
            total_size += v
    if name:
        all_sizes.append((name, total_size))

    return total_size

rs = [
    ('^\$ cd (.*)$', cd),
    ('^\$ ls$', None),
    ('^dir (.*)$', None),
    ('^([0-9]+) (.*)$', size)
]

tree = {}
path = []

for l in f.readlines():
    l = l.rstrip()
    for (idx, r) in enumerate(rs):
        m = re.match(r[0], l)
        if (m):
            if r[1]:
                (tree, path) = r[1](m, tree, path)

all_sizes = []
total_sizes = get_total_size(None, tree, all_sizes)

d = dict(all_sizes)

available = TOTAL_SPACE - d['/']
need_to_free = NEEDED_SPACE - available

bigger = filter(lambda x: x[1] >= need_to_free, all_sizes)
sorted_bigger = sorted(bigger, key=lambda x: x[1])
print(list(sorted_bigger)[0][1])