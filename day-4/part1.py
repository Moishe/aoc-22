def contains(r1, r2):
    return r1[0] >= r2[0] and r1[1] <= r2[1]

f = open('input.txt')
c = 0
for l in f.readlines():
    (range1,range2) = [[int(x) for x in x.split('-')] for x in l.strip().split(',')]
    if contains(range1, range2) or contains(range2, range1):
        c += 1

print(c)
