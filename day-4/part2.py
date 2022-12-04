def overlaps(r1, r2):
    return r1[1] >= r2[0] and r2[1] >= r1[0]

f = open('input.txt')
c = 0
for l in f.readlines():
    (range1,range2) = [[int(x) for x in x.split('-')] for x in l.strip().split(',')]
    if overlaps(range1, range2) or overlaps(range2, range1):
        print(range1, range2)
        c += 1

print(c)
