import re

def is_correct(s):
    pattern = "(\d+)-(\d+) (\w): (\w+)"

    match = re.search(pattern, s)
    min_n = int(match.groups(0)[0])
    max_n = int(match.groups(0)[1])
    letter = match.groups(0)[2]
    password = match.groups(0)[3]

    return (min_n <= password.count(letter) <= max_n)

def is_correct2(s):
    pattern = "(\d+)-(\d+) (\w): (\w+)"

    match = re.search(pattern, s)
    idx1 = int(match.groups(0)[0])
    idx2 = int(match.groups(0)[1])
    letter = match.groups(0)[2]
    password = match.groups(0)[3]

    return ((password[idx1 - 1] == letter) ^ (password[idx2 - 1] == letter))

with open("input.txt", "r") as f:
    input_arr = [n.strip("\n") for n in  f.readlines()]

c = 0
for s in input_arr:
    if is_correct2(s):
        c += 1

print(c)