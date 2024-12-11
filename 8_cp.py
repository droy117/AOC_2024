import math
with open('8.txt') as file:
    grid = file.readlines()

grid = [list(i.strip()) for i in grid]

with open('8_ex_ans.txt') as file:
    grid2 = file.readlines()

grid2 = [list(i.strip()) for i in grid2]

antennas = {}

def traverse_diagonals_lr():
    rows = len(grid)
    cols = len(grid[0])
    
    for c in range(cols):
        i, j = 0, c
        while i < rows and j >= 0:
            if grid[i][j].isalnum(): 
                if grid[i][j] not in antennas:
                    antennas[grid[i][j]] = []
                antennas[grid[i][j]].append([i, j])
            i += 1
            j -= 1

    for r in range(1, rows):
        i, j = r, cols - 1
        while i < rows and j >= 0:
            if grid[i][j].isalnum(): 
                if grid[i][j] not in antennas:
                    antennas[grid[i][j]] = []
                antennas[grid[i][j]].append([i, j])
            i += 1
            j -= 1

traverse_diagonals_lr()
print(antennas)


def find_antinodes_diagonally():
    count = 0
    for v in antennas.values():
        k=0
        print(v)
        l = len(grid)
        for i in v:
            # vv = v[k:]
            # k+=1
            for j in v:
                # hyp = int(math.sqrt((i[1]-j[1])**2 + (i[0]-j[0])**2)) # gives the dist of x axis
                hyp = abs(i[0]-j[0])
                dist = abs(i[0]-j[0]) # gives the dist of y axis
                if hyp > 0:
                    # base = int(math.sqrt(hyp**2 - dist**2)) if int(math.sqrt(hyp**2 - dist**2)) > 0 else dist
                    base = abs(i[1]-j[1])
                    if i[0] > j[0] and i[1] < j[1]:
                        if j[0]-hyp>=0 and j[1]+base<l and grid[j[0]-hyp][j[1]+base] != '#':
                            grid[j[0]-hyp][j[1]+base] = '#'
                            count += 1
                        if i[0]+hyp<l and i[1]-base>=0 and grid[i[0]+hyp][i[1]-base] != '#':
                            grid[i[0]+hyp][i[1]-base] = '#'
                            count+=1
                    if i[0] > j[0] and i[1] > j[1]:
                        if i[0]+hyp<l and i[1]+base<l and grid[i[0]+hyp][i[1]+base] != '#':
                            grid[i[0]+hyp][i[1]+base] = '#'
                            count += 1
                        if j[0]-hyp>=0 and j[1]-base>=0 and grid[j[0]-hyp][j[1]-base] != '#':
                            grid[j[0]-hyp][j[1]-base] = '#'
                            count += 1
                    if j[0] > i[0] and j[1] < i[1]:
                        if i[0]-hyp>=0 and i[1]+base<l and grid[i[0]-hyp][i[1]+base] != '#':
                            grid[i[0]-hyp][i[1]+base] = '#'
                            count+=1
                        if j[0]+hyp<l and j[1]-base>=0 and grid[j[0]+hyp][j[1]-base] != '#':
                            grid[j[0]+hyp][j[1]-base] = '#'
                            count+=1
                    if j[0] > i[0] and j[1] > i[1] :
                        if i[0]-hyp>=0 and i[1]-base>=0 and grid[i[0]-hyp][i[1]-base] != '#':
                            grid[i[0]-hyp][i[1]-base] = '#'
                            count += 1
                        if j[0]+hyp<l and j[1]+base<l and grid[j[0]+hyp][j[1]+base] != '#':
                            grid[j[0]+hyp][j[1]+base] = '#'
                            count += 1
    return count

count = find_antinodes_diagonally()
print(count)

def find_antinodes_vert_hori(count):
    # hori
    for v in antennas.values():
        l = len(grid)
        for i in v:
            for j in v:
                dist_i = abs(i[0]-j[0])
                dist_j = abs(i[1]-j[1])
                if dist_i == 0:
                    if i[1] > j[1]:
                        if i[1]+dist_j<l:
                            count+=1
                        if j[1]-dist_j>=0:
                            count+=1
                    elif i[1] < j[1]:
                        if i[1]-dist_j>=0:
                            count+=1
                        if j[1]+dist_j<l:
                            count+=1

    # vert
    for v in antennas.values():
        l = len(grid)
        for i in v:
            for j in v:
                dist_i = abs(i[0]-j[0])
                dist_j = abs(i[1]-j[1])
                if dist_j == 0:
                    if i[1] > j[1]:
                        if i[1]+dist_i<l:
                            count+=1
                        if j[1]-dist_i>=0:
                            count+=1
                    elif i[1] < j[1]:
                        if i[1]-dist_i>=0:
                            count+=1
                        if j[1]+dist_i<l:
                            count+=1

    return count

print(find_antinodes_vert_hori(count))
    

with open('8_out.txt', 'w') as f:
    for row in grid:
        s = ''.join(row)+"\n"
        f.write(s)
