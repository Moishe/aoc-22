# A: rock
# B: paper
# C: scissors

xlat = {
    "A": 'r',
    "B": 'p',
    "C": 's'
}

hypothesis = {
    "X": 'r',
    "Y": 'p',
    "Z": 's'
}

play_score = {
    'r': 1,
    'p': 2,
    's': 3
}

results = {
    'rp': 1,
    'rs': -1,
    'ps': 1
}

total_score = 0
f = open('input.txt')
for l in f.readlines():
    game = l.strip()

    moves = game.split(' ');
    moves[0] = xlat[moves[0]]
    moves[1] = hypothesis[moves[1]]

    game_str = ''.join(moves)
    if moves[0] == moves[1]:
        result = 0
    else:
        if game_str in results:
            result = results[game_str]
        else:
            result = -results[''.join(reversed(moves))]

    score = (result + 1) * 3 + play_score[moves[1]]
    total_score += score
    print(moves, game_str, result, score)

print("Total: %d" % total_score)
