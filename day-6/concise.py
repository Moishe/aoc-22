unique_len = 14 # 4 for part 1
l = open('input.txt').readline().rstrip()
subsets = filter(lambda x: len(x[1]) == unique_len, [(i + unique_len, set(l[i:i+unique_len])) for i in range(len(l) - unique_len)])
print(list(subsets)[0][0])
