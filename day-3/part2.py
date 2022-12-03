import functools

def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

f = open('input.txt')
sum = 0
items = []
for l in f.readlines():
    contents = set(l.strip())
    items.append(contents)
    if len(items) == 3:
        same = functools.reduce(lambda x,y: x & y, items)
        items = []
        sum += priority(list(same)[0])

print(sum)
