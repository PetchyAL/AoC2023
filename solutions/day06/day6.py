with open('input.txt') as f:
    time, distance = [l.split()[1:] for l in f.read().strip().split('\n')]
    time_p1, distance_p1 = list(map(int, time)), list(map(int, distance))
    time_p2, distance_p2 = int(''.join(time)), int(''.join(distance))

#Part 1
result_p1 = 1
for i, t in enumerate(time_p1):
    for x in range(t):
        if (t - x) * x > distance_p1[i]:
            result_p1 *= (t - x) - x + 1
            break
#Part 2
for x in range(time_p2):
    if (time_p2 - x) * x > distance_p2:
        result_p2 = (time_p2 - x) - x + 1
        break

#Results
print(result_p1) #Part 1
print(result_p2) #Part 2
