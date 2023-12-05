def map_section(bounds, next_map):
    next_ranges = []
    bounds = [bounds]
    for m in next_map:
        for i, bound in enumerate(bounds):
            #If bounds completely encapsulated
            if bound[0] >= m[0][0] and bound[1] <= m[0][1]:
                next_ranges.append([(bound[0] - m[0][0]) +  m[1][0], (bound[1] - m[0][0]) + m[1][0]])
                bound[0] = bound[1]
                break
            elif bound[0] < m[0][0] and bound[1] > m[0][1]:
                next_ranges.append([0 + m[1][0], (m[0][1] - m[0][0]) + m[1][0]])
                del bounds[i]
                bounds.extend([[bound[0], m[0][0]], [m[0][1], bound[1]]])
                pass
            #If not complete encapsulation
            if bound[0] >= m[0][0] and bound[0] < m[0][1]:
                next_ranges.append([(bound[0] - m[0][0]) +  m[1][0], (m[0][1] - m[0][0]) +  m[1][0]])
                bound[0] = m[0][1]
            elif bound[1] >= m[0][0] and bound[1] <= m[0][1]:
                next_ranges.append([0 +  m[1][0], (bound[1] - m[0][0]) +  m[1][0]])
                bound[1] = m[0][0]
    #No bound overlap
    for bound in bounds:
        if bound[0] != bound[1]:
            next_ranges.append([bound[0], bound[1]])
    return next_ranges

with open('input.txt') as f:
    maps = f.read().split('\n\n')
    seeds, maps = maps[0].split()[1:], maps[1:]
    for i, m in enumerate(maps):
        maps[i] = m.split('\n')[1:]
        maps[i] = [[[s, s + r], [d, d + r]] 
                        for d, s, r in [map(int, x.split()) for x in maps[i]]]

part_one, part_two = [], []
for i in range(len(seeds)):
    part_one.append([int(seeds[i]), int(seeds[i]) + 1])
    if i % 2 == 0:
        part_two.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])])
for m in maps:
    part_one = sum(list(map(map_section, part_one, [m]*len(part_one))), [])
    part_two = sum(list(map(map_section, part_two, [m]*len(part_two))), [])

#Results
print(min([x[0] for x in part_one])) #Part 1
print(min([x[0] for x in part_two])) #Part 2
