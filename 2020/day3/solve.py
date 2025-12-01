
class Map:

  def __init__(self, map_lines):
    self.data = map_lines
    self.width = len(map_lines[0])
    self.height = len(map_lines)

  def at(self, x, y):
    return self.data[y][x % self.width]





with open("input.txt", "r") as f:
  mapa = Map([l.strip("\n") for l in f.readlines()])



slopes = [
  (1, 1),
  (3, 1),
  (5, 1),
  (7, 1),
  (1, 2),
]

multiplied = 1

for s in slopes:
  x = 0
  y = 0
  encounters = 0
  for i in range(0, mapa.height, s[1]):
    if mapa.at(x, y) == "#":
      encounters += 1
    x += s[0]
    y += s[1]
  multiplied *= encounters
  print("Right {0}, down {1}: {2}".format(s[0], s[1], encounters))

print("Multiplied: {0}", multiplied)


