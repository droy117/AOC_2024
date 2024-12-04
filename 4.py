string = ""
with open('4.txt') as file:
    string = file.readlines()

grid = []
for s in string:
    lst = []
    s = s.strip()
    for char in s:
        lst.append(char)
    grid.append(lst)

count = 0
h, v, hn, vn, dr, dl, ur, ul = 0,0,0,0,0,0,0,0
l = len(grid)
# for i in range(0, l):
#     for j in range(0, l):
#         if grid[i][j] == 'X':
#             # hori x
#             if j+1<l and grid[i][j+1] == 'M':
#                 if j+2<l and grid[i][j+2] == 'A':
#                     if j+3<l and grid[i][j+3] == 'S':
#                         h += 1
#                         count += 1
#             # vert y
#             if i+1<l and grid[i+1][j] == 'M':
#                 if i+2<l and grid[i+2][j] == 'A':
#                     if i+3<l and grid[i+3][j] == 'S':
#                         v += 1
#                         count += 1
#             # hori -x
#             if j-1>=0 and grid[i][j-1] == 'M':
#                 if j-2>=0 and grid[i][j-2] == 'A':
#                     if j-3>=0 and grid[i][j-3] == 'S':
#                         hn += 1
#                         count += 1
#             # vert -y
#             if i-1>=0 and grid[i-1][j] == 'M':
#                 if i-2>=0 and grid[i-2][j] == 'A':
#                     if i-3>=0 and grid[i-3][j] == 'S':
#                         vn += 1
#                         count += 1
            
#             # dig down-right
#             if i+1<l and j+1<l and grid[i+1][j+1] == 'M':
#                 if i+2<l and j+2<l and grid[i+2][j+2] == 'A':
#                     if i+3<l and j+3<l and grid[i+3][j+3] == 'S':
#                         dr += 1
#                         count += 1
            
#             # dig down-left
#             if i+1<l and j-1>=0 and grid[i+1][j-1] == 'M':
#                 if i+2<l and j-2>=0 and grid[i+2][j-2] == 'A':
#                     if i+3<l and j-3>=0 and grid[i+3][j-3] == 'S':
#                         dl += 1
#                         count += 1
            
#             # dig up-right
#             if i-1>=0 and j+1<l and grid[i-1][j+1] == 'M':
#                 if i-2>=0 and j+2<l and grid[i-2][j+2] == 'A':
#                     if i-3>=0 and j+3<l and grid[i-3][j+3] == 'S':
#                         ur += 1
#                         count += 1
            
#             # dig up-left
#             if i-1>=0 and j-1>=0 and grid[i-1][j-1] == 'M':
#                 if i-2>=0 and j-2>=0 and grid[i-2][j-2] == 'A':
#                     if i-3>=0 and j-3>=0 and grid[i-3][j-3] == 'S':
#                         ul += 1
#                         count += 1

# print(count)

for i in range(0, l):
    for j in range(0, l):
        if grid[i][j] == 'A':
            # pat 1
            if i-1>=0 and j-1>=0 and grid[i-1][j-1] == 'M':
                if i+1<l and j+1<l and grid[i+1][j+1] == 'S':
                    if i+1<l and j-1>=0 and grid[i+1][j-1] == 'M':
                        if i-1>=0 and j+1<l and grid[i-1][j+1] == 'S':
                            count += 1

            # pat 2
            if i-1>=0 and j-1>=0 and grid[i-1][j-1] == 'M':
                if i+1<l and j+1<l and grid[i+1][j+1] == 'S':
                    if i+1<l and j-1>=0 and grid[i+1][j-1] == 'S':
                        if i-1>=0 and j+1<l and grid[i-1][j+1] == 'M':
                            count += 1
            
            # pat 3
            if i-1>=0 and j-1>=0 and grid[i-1][j-1] == 'S':
                if i+1<l and j+1<l and grid[i+1][j+1] == 'M':
                    if i+1<l and j-1>=0 and grid[i+1][j-1] == 'S':
                        if i-1>=0 and j+1<l and grid[i-1][j+1] == 'M':
                            count += 1

            # pat 4
            if i-1>=0 and j-1>=0 and grid[i-1][j-1] == 'S':
                if i+1<l and j+1<l and grid[i+1][j+1] == 'M':
                    if i+1<l and j-1>=0 and grid[i+1][j-1] == 'M':
                        if i-1>=0 and j+1<l and grid[i-1][j+1] == 'S':
                            count += 1

print(count)