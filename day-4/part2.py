f = open('input.txt')
o = [[[int(x) for x in r.split('-')] for r in l.strip().split(',')] for l in f.readlines()]
m = filter(lambda x: x[0][1] >= x[1][0] and x[1][1] >= x[0][0], o)
print(len(list(m)))
