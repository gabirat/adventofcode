import re
import sys

with open("day6/input.txt", "r") as f:
  groups = f.read().split("\n\n")

ts = []

for g in groups:
  groups[groups.index(g)] = g.split("\n")

del g
#part1
s = 0
for g in groups:
  ans = {}
  for p in g:
    for a in p:
      ans[a] = 1
  for a in ans:
    s += ans[a]

print(s)
#part2
s = 0
for g in groups:
  ans = {}
  for p in g:
    for a in p:
      ans[a] = ans[a] + 1 if a in ans else 1
  for a in ans:
    if ans[a] == len(g):
      s += 1

print(s)


  



