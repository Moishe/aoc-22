import json
f = open('input.txt')
pairs = [[json.loads(s) for s in l.split('\n')]
         for l in f.read().split('\n\n')]


def compare(pair):
    (left, right) = pair
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1

    if type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]

    for i in range(min(len(left), len(right))):
        r = compare([left[i], right[i]])
        if r != 0:
            return r

    if len(left) < len(right):
        return -1
    elif len(right) < len(left):
        return 1
    else:
        return 0


results = filter(lambda x: x[1] == -1, [(result[0] + 1,
                 compare(result[1])) for result in enumerate(pairs)])
print(sum([x[0] for x in results]))
