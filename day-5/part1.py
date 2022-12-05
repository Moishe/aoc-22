import re
from collections import defaultdict, deque
f = open('input.txt')

state = 0 # 0 is stacks; 1 is moves
stacks = defaultdict(deque)
stack_count = None
for l in f.readlines():
    l = l[:-1]
    if len(l) == 0:
        state += 1
        continue

    if state == 0:
        stack_count = int(len(l) / 4)
        for i in range(int(len(l) / 4) + 1):
            idx = i * 4 + 1
            if str.isalpha(l[idx]):
                stacks[i + 1].append(l[idx])
    else:
        m = re.match('move (\d+) from (\d+) to (\d+)', l)
        if m:
            (count, source, dest) = [int(x) for x in m.group(1,2,3)]
            for i in range(count):
                stacks[dest].appendleft(stacks[source].popleft())
        else:
            print("!!!", l)
            exit(1)

result = ''
for i in range(stack_count + 1):
    result += stacks[i + 1][0]

print(result)