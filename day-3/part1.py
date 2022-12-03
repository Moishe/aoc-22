def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

f = open('input.txt')
sum = 0
for l in f.readlines():
    contents = l.strip()
    mid = int(len(contents) / 2)
    (a, b) = (set(contents[:mid]), set(contents[mid:]))
    sum += priority(list(a & b)[0])

print(sum)