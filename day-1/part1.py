f = open('input.txt')

total = 0
mx = 0
for l in f.readlines():
    if len(l) == 1:
        mx = max(mx, total)
        total = 0
    else:
        total += int(l)

print(mx)
    
