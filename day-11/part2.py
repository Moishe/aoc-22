from collections import defaultdict
import functools
import math
import json
import re
"""
def primefactors(i):
    if i == 2:
        return set([2])

    factors = set()
    for x in range(2, int(math.sqrt(i)) + 1):
        if i % x == 0:
            factors.add(x)
            factors.update(primefactors(int(i / x)))
    if not len(factors):
        factors.add(i)
    return set(factors)
"""
def getmonkeystate(s):
    lines = s.split('\n')
    monkeyId = int(re.match('Monkey ([0-9])+:', lines[0]).groups(1)[0])
    items = [int(x) for x in re.match('  Starting items: (.*)', lines[1]).groups(1)[0].split(', ')]
    (operation, operand) = re.match('  Operation: new = old (.*) (.*)', lines[2]).groups()
    (test, testnumber) = re.match('  Test: (.*) by ([0-9]+)', lines[3]).groups()
    testnumber = int(testnumber)
    (trueDest) = int(re.match('    If true: throw to monkey ([0-9]+)', lines[4]).groups(1)[0])
    (falseDest) = int(re.match('    If false: throw to monkey ([0-9]+)', lines[5]).groups(1)[0])
    monkeystate = {
        'monkeyId': monkeyId,
        'items': items,
        'operation': operation,
        'operand': operand,
        'test': test,
        'testnumber': testnumber,
        'trueDest': trueDest,
        'falseDest': falseDest,
        'inspections': 0
    }
    return monkeystate

def mul(x,y):
    if y in x:
        x[y] = 0
    return x

def add(x,y):
    for z in x.keys():
        x[z] = (x[z] + y) % z
    return x

operations = {
    '+': lambda x,y: add(x,y),
    '*': lambda x,y: mul(x,y)
}

tests = {
    'divisible': lambda x,y: x[y] == 0
}

def prepmonkeystate(monkeystates_list, monkeystate):
    divisors = [x['testnumber'] for x in monkeystates_list]
    new_items = []
    for item in monkeystate['items']:
        remainders = {}
        for divisor in divisors:
            remainders[divisor] = item % divisor
        new_items.append(remainders)

    monkeystate['new_items'] = new_items
    return monkeystate

def proc_monkey(id, monkeystates):
    monkey = monkeystates[id]
    for item in monkey['items']:
        monkey['inspections'] += 1
        if monkey['operand'] == 'old':
            pass
            #new_item = new_operations[monkey['operation']](item, item)
        else:
            new_item = operations[monkey['operation']](item, int(monkey['operand']))
            print(item, new_item, monkey['operation'], monkey['operand'])
        evaluation = tests[monkey['test']](item, int(monkey['testnumber']))
        print(evaluation, monkey['testnumber'])
        if evaluation:
            monkeystates[monkey['trueDest']]['items'].append(item)
        else:
            monkeystates[monkey['falseDest']]['items'].append(item)
    monkey['items'] = []

monkeystates_list = [getmonkeystate(x) for x in open('/Users/moishelettvin/src/aoc-22/day-11/sample-input.txt').read().split('\n\n')]
monkeystates = {}
for monkeystate in monkeystates_list:
    monkeystates[monkeystate['monkeyId']] = prepmonkeystate(monkeystates_list, monkeystate)
monkeystates_list = None
for i in range(1):
    if i % 100 == 0:
        inspections = list(sorted([int(x['inspections']) for x in monkeystates.values()]))
        print(inspections)
    for id in range(len(monkeystates.items())):
        proc_monkey(id, monkeystates)

inspections = list(sorted([int(x['inspections']) for x in monkeystates.values()]))[-2:]
print(inspections)
print(functools.reduce(lambda x, y: x * y, inspections))