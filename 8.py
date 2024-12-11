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
print(antennas.keys())


def find_antinodes_diagonally():
    for v in antennas.values():
        # k=1
        print(v)
        l = len(grid)
        for i in v:
            # vv = v[k:]
            # k+=1
            for j in v:
                dist = abs(i[0]-j[0])
                if dist > 0:
                    base = abs(i[1]-j[1])
                    if i[0] > j[0] and i[1] < j[1]:
                        x1=i[0]+dist
                        x2=j[0]-dist
                        y1=i[1]-base
                        y2=j[1]+base
                        while x2>=0 and y2<l:
                            grid[x2][y2] = '#' if grid[x2][y2] == '.' else grid[x2][y2]
                            x2-=dist
                            y2+=base
                        while x1<l and y1>=0:
                            grid[x1][y1] = '#' if grid[x1][y1] == '.' else grid[x1][y1]
                            x1+=dist
                            y1-=base
                    if i[0] > j[0] and i[1] > j[1]:
                        x1=i[0]+dist
                        x2=j[0]-dist
                        y1=i[1]+base
                        y2=j[1]-base
                        while x1<l and y1<l:
                            grid[x1][y1] = '#' if grid[x1][y1] == '.' else grid[x1][y1]
                            x1+=dist
                            y1+=base
                        while x2>=0 and y2>=0:
                            grid[x2][y2] = '#' if grid[x2][y2] == '.' else grid[x2][y2]
                            x2-=dist
                            y2-=base
                    if j[0] > i[0] and j[1] < i[1]:
                        x1=i[0]-dist
                        x2=j[0]+dist
                        y1=i[1]+base
                        y2=j[1]-base
                        while x1>=0 and y1<l:
                            grid[x1][y1] = '#' if grid[x1][y1] == '.' else grid[x1][y1]
                            x1-=dist
                            y1+=base
                        while x2<l and y2>=0:
                            grid[x2][y2] = '#' if grid[x2][y2] == '.' else grid[x2][y2]
                            x2+=dist
                            y2-=base
                    if j[0] > i[0] and j[1] > i[1] :
                        x1=i[0]-dist
                        x2=j[0]+dist
                        y1=i[1]-base
                        y2=j[1]+base
                        while x1>=0 and y1>=0:
                            grid[x1][y1] = '#' if grid[x1][y1] == '.' else grid[x1][y1]
                            x1-=dist
                            y1-=base
                        while x2<l and y2<l:
                            grid[x2][y2] = '#' if grid[x2][y2] == '.' else grid[x2][y2]
                            x2+=dist
                            y2+=base

find_antinodes_diagonally()
count=0
for row in grid:
    for i in row:
        if i == '#' or i.isalnum():
            count+=1

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
                        x1=i[1]+dist_j
                        x2=j[1]-dist_j
                        while x1<l:
                            count+=1
                            x1+=dist_j
                        while x2>=0:
                            count+=1
                            x2-=dist_j
                    elif i[1] < j[1]:
                        x1=i[1]-dist_j
                        x2=j[1]+dist_j
                        while i[1]-dist_j>=0:
                            count+=1
                            x1-=dist_j
                        while j[1]+dist_j<l:
                            count+=1
                            x2+=dist_j

    # vert
    for v in antennas.values():
        l = len(grid)
        for i in v:
            for j in v:
                dist_i = abs(i[0]-j[0])
                dist_j = abs(i[1]-j[1])
                if dist_j == 0:
                    if i[1] > j[1]:
                        x1=i[1]+dist_i
                        x2=j[1]-dist_i
                        while x1<l:
                            count+=1
                            x1+=dist_i
                        while x2>=0:
                            count+=1
                            x2-=dist_i
                    elif i[1] < j[1]:
                        x1=i[1]-dist_i
                        x2=j[1]+dist_i
                        while x1>=0:
                            count+=1
                            x1-=dist_i
                        while x2<l:
                            count+=1
                            x2+=dist_i

    return count

print(find_antinodes_vert_hori(count))
    

with open('8_out.txt', 'w') as f:
    for row in grid:
        s = ''.join(row)+"\n"
        f.write(s)
