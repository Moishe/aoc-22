import json
import re

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
            size_node[k] = get_total_size(k, v, all_sizes)
            total_size += size_node[k][0]
        else:
            total_size += v
    all_sizes.append((name, total_size))
    return (total_size, size_node)

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

print(json.dumps(tree, indent=2))

all_sizes = []
total_sizes = get_total_size('root', tree, all_sizes)
print(all_sizes)
print(json.dumps(total_sizes, indent=2))

smaller = filter(lambda x: x <= 100000, [x[1] for x in all_sizes])
print(sum(smaller))

