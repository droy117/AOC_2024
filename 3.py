import re
new_string = ""
with open('3.txt') as file:
    string = file.readlines()

    string = " ".join(string)

    strings = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', string)

    print(strings)

def mul(x,y):
    return x*y

sum = 0
ok = True
for s in strings:
    if ok and s.startswith("mul"):
        x, y = map(int, re.search(r'mul\((\d+),(\d+)\)', s).groups())
        sum += mul(x, y)
    if s == 'do()':
        ok = True
        continue
    if s == "don't()":
        ok = False

print(sum)