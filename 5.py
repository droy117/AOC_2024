with open('5.txt') as file:
    pairs = []
    orders = []

    for line in file:
        line = line.strip()
        if '|' in line:
            x, y = line.split('|')
            z = (x,y)
            pairs.append(z)
        if ',' in line:
            line = line.split(',')
            orders.append(line)

print(orders)
incorrect_orders = []
sum = 0
for order in orders:
    print(order)
    count = 0
    for i in range(0, len(order)-1):
        z = (order[i], order[i+1])
        print(z)
        if z in pairs:
            count += 1
    if count == len(order)-1:
        mid = len(order)//2
        sum += int(order[mid])
    else:
        incorrect_orders.append(order)
    count = 0

print(pairs)
print(orders)
print(incorrect_orders)

print(sum)

sum = 0

while True:
    swap = 0
    sum = 0
    for order in incorrect_orders:
        for i in range(0, len(order)-1):
            z = (order[i], order[i+1])
            iz = (order[i+1], order[i])
            if z in pairs:
                continue
            if z not in pairs and iz in pairs:
                swap = 1
                temp = order[i+1]
                order[i+1] = order[i]
                order[i] = temp
            
        mid = len(order)//2
        sum += int(order[mid])
    if swap == 0:
        break

print(incorrect_orders)
print(sum)
