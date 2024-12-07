from itertools import product

with open('7.txt') as file:
    values = file.readlines()

nums = []
for value in values:
    splits = value.split(":")
    splits = splits[0]+splits[1]
    nums.append([int(i) for i in splits.strip().split()])

def generate_combinations(n):
    characters = ['+', '*', '|']
    combinations = [''.join(p) for p in product(characters, repeat=n)]
    return combinations


def evaluate(lst, op):
    val = lst[0]
    k = 0
    for i in lst[1:]:
        if op[k] == '+':
            val += i
        elif op[k] == '*':
            val *= i
        else:
            val = int(f"{val}{i}")
        k += 1
    return val

s = 0
for i in range(0, len(nums)):
    tv = nums[i][0]
    ops = generate_combinations(len(nums[i])-2)
    for op in ops:
        if evaluate(nums[i][1:], op) == tv:
            s += tv
            break

print(s)
        