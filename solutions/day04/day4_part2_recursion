def get_reward(c, r, rewards):
    result = r
    for card in range(c, c + r):
        result += get_reward(card + 1, rewards[card + 1], rewards)
    return result

with open('input.txt') as f:
    cards = f.read().strip().split('\n')
    cards = [card.split(': ')[1] for card in cards]
    cards = [card.split(' | ') for card in cards]

rewards = {}
for c in range(len(cards)):
    matching_numbers = 0
    winning, own = cards[c][0].split(), cards[c][1].split()
    for num in winning:
        matching_numbers += 1 if num in own else 0
    rewards[c] = matching_numbers

total_cards = len(cards)
for c, r in rewards.items():
    total_cards += get_reward(c, r, rewards)

print(total_cards) #Result
