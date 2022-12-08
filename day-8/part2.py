import functools

visibility = set()
rows = []
columns = []

def dist(a,m):
    for (idx, v) in enumerate(a):
        if v >= m:
            return idx+1
    return len(a)

f = open('input.txt')
for (rowidx, l) in enumerate([l.strip() for l in f.readlines()]):
    width = len(l)
    rows.append([int(i) for i in l])
    for (i, v) in enumerate(rows[-1]):
        if len(columns) <= i:
            columns.append([v])
        else:
            columns[i].append(v)

score = 0
for y in range(len(rows)):
    row = rows[y]
    for x in range(len(columns)):
        column = columns[x]
        l = list(reversed(row[0:x]))
        r = row[x+1:]
        u = list(reversed(column[0:y]))
        d = column[y+1:]
        dists = [dist(a, row[x]) for a in [l, r, u, d]]
        score = max(score, functools.reduce(lambda a,b: a * b, dists, 1))

print(score)
