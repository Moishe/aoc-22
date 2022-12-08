import functools

visibility = set()
rows = []
columns = []

f = open('input.txt')
for (rowidx, l) in enumerate([l.strip() for l in f.readlines()]):
    width = len(l)
    rows.append([(int(i[1]), rowidx * width + i[0])  for i in enumerate(l)])
    for (i, v) in enumerate(rows[-1]):
        if len(columns) <= i:
            columns.append([v])
        else:
            columns[i].append(v)

for row in rows:
    visibility.update([x[1] for x in functools.reduce(lambda x,b: x + [b] if not len(x) or b[0] > max([y[0] for y in x]) else x, row, [])])
    visibility.update([x[1] for x in functools.reduce(lambda x,b: x + [b] if not len(x) or b[0] > max([y[0] for y in x]) else x, reversed(row), [])])

for col in columns:
    visibility.update([x[1] for x in functools.reduce(lambda x,b: x + [b] if not len(x) or b[0] > max([y[0] for y in x]) else x, col, [])])
    visibility.update([x[1] for x in functools.reduce(lambda x,b: x + [b] if not len(x) or b[0] > max([y[0] for y in x]) else x, reversed(col), [])])

print(visibility, len(visibility))
