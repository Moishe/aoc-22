import json
from functools import cmp_to_key
f = open('input.txt')
pairs = [[json.loads(s) for s in l.split('\n')]
         for l in f.read().split('\n\n')]


def compare(left, right=None):
    if right == None:
        return -1
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1

    if type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]

    for i in range(min(len(left), len(right))):
        r = compare(left[i], right[i])
        if r != 0:
            return r

    if len(left) < len(right):
        return -1
    elif len(right) < len(left):
        return 1
    else:
        return 0


packets = [packet for pair in pairs for packet in pair]
packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key=cmp_to_key(compare))
two_idx = None
six_idx = None
for (idx, packet) in enumerate(packets):
    if packet == [[2]]:
        two_idx = idx + 1
    elif packet == [[6]]:
        six_idx = idx + 1
print(six_idx * two_idx)
