def get_num(row, c):
    while True:
        if not row[c-1].isnumeric():
            break
        else: c -= 1
    num = ""
    for i in range(c, len(row)-1):
        if row[i].isnumeric():
            num = num + row[i]
        else: break
    return int(num)

def check_neighbours(r, c, schematic):
    return {
        'N': schematic[r-1][c], 'S': schematic[r+1][c],
        'E': schematic[r][c+1], 'W': schematic[r][c-1],
        'NE': schematic[r-1][c+1], 'SE': schematic[r+1][c+1],
        'NW': schematic[r-1][c-1], 'SW': schematic[r+1][c-1]
        }

with open('input.txt') as f:
    lines = f.read().strip().split('\n')
    lines.append("."*len(lines[0]))
    lines.insert(0, "."*len(lines[0]))
    for line in range(len(lines)):
      lines[line] = '.' + lines[line] + '.'

parts = []
num = ""
valid = False
gear_ratios = []

for line in range(1, len(lines)-1):
    for char in range(1,len(lines[line])-1):
      
        #Part 1
        if lines[line][char].isnumeric():
            num = num + lines[line][char]
            nb = check_neighbours(line, char, lines)
            if any((not(c.isalnum()) and c != '.') for c in nb.values()):
                valid = True
        else:
            if num != "" and valid:
                parts.append(int(num))
            valid = False
            num = ""
          
        #Part 2
        if lines[line][char] == '*':
            adj = []
            nb = {d: val.isnumeric() for d, val in check_neighbours(line, char, lines).items()}
            if nb['E']: adj.append(get_num(lines[line], char+1))
            if nb['W']: adj.append(get_num(lines[line], char-1))
            if nb['N']: adj.append(get_num(lines[line-1], char))
            if nb['S']: adj.append(get_num(lines[line+1], char))
            if nb['NW'] and not nb['N']: adj.append(get_num(lines[line-1], char-1))
            if nb['NE'] and not nb['N']: adj.append(get_num(lines[line-1], char+1))
            if nb['SW'] and not nb['S']: adj.append(get_num(lines[line+1], char-1))
            if nb['SE'] and not nb['S']: adj.append(get_num(lines[line+1], char+1))
            if len(adj) != 2:
                continue
            gear_ratios.append(adj[0]*adj[1])
        else: continue

#Results
print(sum(parts)) #Part 1
print(sum(gear_ratios)) #Part 2
