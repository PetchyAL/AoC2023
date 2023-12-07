def get_type(hand, strength):
    counts = []
    jokers = 0
    for c in strength:
        if c == 'J':
            jokers = hand.count(c)
        else: counts.append(hand.count(c)) if c in hand else 0
    if not counts: return 6
    if max(counts) + jokers in [4, 5]:
        return max(counts) + jokers + 1
    elif len(counts) == 2 and max(counts) + jokers == 3: 
        return 4
    elif len(counts) in [2, 3]:
        if any([x + jokers == 3 for x in counts]): 
            return 3
        else: return 2
    elif len(counts) in [3, 4] and max(counts) + jokers == 2: 
        return 1
    else: return 0

STRENGTH = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
groups = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': []}

with open('input.txt') as f:
    hands = f.read().strip().split('\n')
    hands = [hand.split() for hand in hands]
    hands = [[hand[0], int(hand[1])] for hand in hands]
    
result = 0
for i, t in enumerate(map(get_type, [''.join(hand[0]) for hand in hands], [STRENGTH]*len(hands))):
    groups[str(t)].append(hands[i])
for k in groups.keys():
    groups[k] = sorted(groups[k], key=lambda x: [STRENGTH.index(c) for c in x[0]])

rank = 1
for group in groups.values():
    for hand in group:
        result += rank * hand[1]
        rank += 1
print(result)
