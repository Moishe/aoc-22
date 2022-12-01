f = open('input.txt')

total = 0
totals = []
for l in f.readlines():
    if len(l) == 1:
        totals.append(total)
        total = 0
    else:
        total += int(l)

totals.append(total)

totals.sort(reverse=True)
print(totals[:3])
print(sum(totals[:3]))
    
