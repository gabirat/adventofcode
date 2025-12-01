from itertools import combinations

with open("input.txt") as f:
    input = [int(n) for n in f.readlines()]

all_comb = combinations(input, 2)

for c in all_comb:
    if c[0] + c[1] == 2020:
        print("a={0}, b={1} | a*b={2}".format(c[0], c[1], c[0] * c[1]))
        break

all_comb = combinations(input, 3)

for c in all_comb:
    if c[0] + c[1] + c[2] == 2020:
        print("a={0}, b={1}, c={2} | a*b*c={3}".format(c[0], c[1], c[2], c[0] * c[1] * c[2]))
        break