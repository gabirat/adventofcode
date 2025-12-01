import re
import sys

def get_seat_id(seat):
  return seat[0] * 8 + seat[1]

def get_row(r):
  rows = range(128)
  for fb in r:
    if fb == "F":
      rows = rows[0:int(len(rows)/2)]
    if fb == "B":
      rows = rows[int(len(rows)/2)::]
  return rows[0]

def get_col(c):
  cols = range(8)
  for rl in c:
    if rl == "L":
      cols = cols[0:int(len(cols)/2)]
    if rl == "R":
      cols = cols[int(len(cols)/2)::]
  return cols[0]


def get_seat(s):
  m = re.match("(?P<rows>[FB]{7})(?P<cols>[LR]{3})", s)
  rows = m.group("rows")
  cols = m.group("cols")
  return (get_row(rows), get_col(cols))

def print_plane(seat_touples):
  sets_ordered = [None] * (128 * 8)
  for s in seat_touples:
    sets_ordered[s[0] * 8 + s[1]] = s
  print("+01234567")
  for y in range(128):
    sys.stdout.write("{:03d}".format(y))
    for x in range(8):
      if sets_ordered[y * 8 + x] is not None:
        sys.stdout.write("#")
      else:
        sys.stdout.write("$")
    sys.stdout.write("\n")

with open("day5/input.txt", "r") as f:
  seats = f.read().split("\n")
  seats = [s.strip("\n") for s in seats]

seats = [get_seat(s) for s in seats]

max_id = max([get_seat_id(s) for s in seats])
print("Max is: {0}".format(max_id))

print_plane(seats)

  



