with open('input.txt') as f:
    cards = f.read().strip().split('\n')
    cards = [card.split(': ')[1] for card in cards]
    cards = [card.split(' | ') for card in cards]

points = 0
card_reward = [1] * len(cards)

for c in range(len(cards)):
    matching_numbers = 0
    winning, own = cards[c][0].split(), cards[c][1].split()
    for num in winning:
        matching_numbers += 1 if num in own else 0
    if matching_numbers > 0:
        points += pow(2, matching_numbers - 1)
        for r in range(c, c + matching_numbers):
            if r + 1 < len(cards):
                card_reward[r + 1] += card_reward[c]
            else: break
                
#Results
print(points) #Part 1
print(sum(card_reward)) #Part 2
