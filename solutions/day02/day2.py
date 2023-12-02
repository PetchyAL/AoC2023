def check_game(game):
    for g_set in game[1].split('; '):
        bag = {'red': 12, 'green': 13, 'blue': 14}
        for subset in g_set.split(', '):
            val = subset.split(' ')
            bag[val[1]] -= int(val[0])
        if any(colour < 0 for colour in bag.values()):
            return False
        else: continue
    return True

def get_power(game):
    bag = {'red': 0, 'green': 0, 'blue': 0}
    for g_set in game[1].split('; '):
        for subset in g_set.split(', '):
            val = subset.split(' ')
            if bag[val[1]] < int(val[0]):
                bag[val[1]] = int(val[0])
    return bag['red'] * bag['green'] * bag['blue']

#File parsing
with open('input.txt') as f:
    lines = f.read().strip().split('\n')
    lines = [line.split(': ') for line in lines]
    for line in lines: 
        line[0] = int(line[0].split(' ')[-1])

valid_games = []
power = 0
for l in lines:
    valid_games.append(l[0]) if check_game(l) else 0
    power += get_power(l)

#Results
print(sum(valid_games)) #Part 1
print(power) #Part 2
