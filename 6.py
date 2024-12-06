import copy
map = []
with open('6.txt') as file:
    for line in file:
        map.append(list(line.strip()))


pos = (0,0)
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == '^':
            map[i][j] = 'X'
            pos = (i, j)
            break

def check_loop(grid, i, j, dir):
    # print("in check loop")
    ini_i, ini_j =  i, j
    win=False
    while True and win==False:
        while dir == 'up':
            # print("in up check")
            if i-1==0 and grid[i-1][j]!='#':
                win=True
                break
            if i-1>=0 and grid[i-1][j]!='#':
                i-=1
            if grid[i][j] == '.':
                return False
            if i-1>=0 and grid[i-1][j]=='#':
                dir='right'
                if (i,j) == (ini_i, ini_j) and j+1<len(grid) and grid[i][j+1]=='X':
                    return True
                break
        while dir=='right':
            # print("in right check")
            if j+1==len(grid)-1 and grid[i][j+1]!='#':
                win=True
                break 
            if j+1<len(grid) and grid[i][j+1]!='#':
                j+=1
            if grid[i][j] == '.':
                return False
            if j+1<len(grid) and grid[i][j+1]=='#':
                dir='down'
                if (i,j) == (ini_i, ini_j) and i+1<len(grid) and grid[i+1][j]=='X':
                    return True
                break
        while dir=='down':
            # print("in down check")
            if i+1==len(grid)-1 and grid[i+1][j]!='#':
                win=True
                break
            if i+1<len(grid) and grid[i+1][j]!='#':
                i+=1
            if grid[i][j] == '.':
                return False
            if i+1<len(grid) and grid[i+1][j]=='#':
                dir='left'
                if (i,j) == (ini_i, ini_j) and j-1>=0 and grid[i][j-1]=='X':
                    return True
                break
        while dir=='left':
            # print("in left check")
            if j-1==0 and grid[i][j-1]!='#':
                win=True
                break
            if j-1>=0 and grid[i][j-1]!='#':
                j-=1
            if grid[i][j] == '.':
                return False
            if j-1>=0 and grid[i][j-1]=='#':
                dir='up'
                if (i,j) == (ini_i, ini_j) and i-1>=0 and grid[i-1][j]=='X':
                    return True
                break

def search(grid):
    # print("in search")
    dir = 'up'
    i, j = pos
    # print("INITIAL POS",(i,j))
    win=False
    while True and win==False:
        while dir == 'up':
            # print("in up")
            if i-1==0 and grid[i-1][j]!='#':
                grid[i-1][j]='X'
                win=True
                break
            if i>=0 and grid[i-1][j]!='#':
                i-=1
                grid[i][j]='X'
            if grid[i-1][j]=='#':
                dir='right'
                if j+1<len(grid) and grid[i][j+1]=='#':
                    dir="down"
                if check_loop(grid, i, j, dir):
                    return True
                break
        while dir=='right':
            # print("in right")
            if j+1==len(grid)-1 and grid[i][j+1]!='#':
                grid[i][j+1]='X'
                win=True
                break        
            if j<len(grid) and grid[i][j+1]!='#':
                j+=1
                grid[i][j]='X'
            if grid[i][j+1]=='#':
                dir='down'
                if i+1<len(grid) and grid[i+1][j]=='#':
                    dir="left"
                if check_loop(grid, i, j, dir):
                    return True
                break
        while dir=='down':
            # print("in down")
            if i+1==len(grid)-1 and grid[i+1][j]!='#':
                grid[i+1][j]='X'
                win=True
                break
            if i<len(grid) and grid[i+1][j]!='#':
                i+=1
                grid[i][j]='X'
            if grid[i+1][j]=='#':
                dir='left'
                if j-1>=0 and grid[i][j-1]=='#':
                    dir="up"
                if check_loop(grid, i, j, dir):
                    return True
                break
        while dir=='left':
            # print("in left")
            if j-1==0 and grid[i][j-1]!='#':
                grid[i][j-1]='X'
                win=True
                break
            if j>=0 and grid[i][j-1]!='#':
                j-=1
                grid[i][j]='X'
            if grid[i][j-1]=='#':
                dir='up'
                if i-1>=0 and grid[i-1][j]=='#':
                    dir="right"
                if check_loop(grid, i, j, dir):
                    return True
                break

def display(grid):
    f = open('log', 'a')
    for line in grid:
        f.write(f"{line}\n")
    f.write("\n\n")


count=0
for i in range(0, len(map)):
    for j in range(0, len(map)):
        map_copy = copy.deepcopy(map)
        map_copy[i][j] = '#'
        # print(map_copy,"\n\n")
        if search(map_copy):
            # display(map_copy)
            count+=1
# print(map)

# search(map)
# for row in map:
#     for p in row:
#         if p=='X':
#             count+=1
# print(map)
print(count)