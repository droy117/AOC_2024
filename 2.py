with open('2.txt') as file:
    inputs = file.readlines()


def check_safety(line):
    count = 0
    differ = True
    for i in range(0, len(line)-1):
        if line[i] > line[i+1]:
            count -= 1
        elif line[i+1] > line[i]:
            count += 1
        
        if abs(line[i]-line[i+1]) <= 0 or abs(line[i]-line[i+1]) > 3:
            differ = False
        
    return abs(count) == (len(line)-1) and differ

def levels():
    safety = 0
    for line in inputs:
        line = list(map(int, line.split()))
        for i in range(0, len(line)):
            if check_safety(line[:i]+line[i+1:]):
                safety += 1
                break
    return safety

print(levels())