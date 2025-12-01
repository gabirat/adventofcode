with open("input.txt", "r") as file:
    data = file.read().splitlines()
    wires_data = []
    for l in data:
        wires_data.append(l.split(","))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_from(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_direction(self):
        return "|" if self.p1.x == self.p2.x else "_"

    def get_intersection(self, other):
        if self.get_direction() == "_":
            if other.get_direction() == "|":
                if ((self.p1.x - other.p1.x <= 0) and (self.p2.x - other.p1.x >= 0)) or ((self.p1.x - other.p1.x >= 0) and (self.p2.x - other.p1.x <= 0)):
                    if ((self.p1.y - other.p1.y <= 0) and (self.p1.y - other.p2.y >= 0)) or ((self.p1.y - other.p1.y >= 0) and (self.p1.y - other.p2.y <= 0)):
                        return Point(other.p1.x, self.p1.y)
                return None
            else:
                return None
        else:
            if other.get_direction() == "_":
                if ((self.p1.x - other.p1.x <= 0) and (self.p1.x - other.p2.x >= 0)) or ((self.p1.x - other.p1.x >= 0) and (self.p1.x - other.p2.x <= 0)):
                    if ((self.p1.y - other.p1.y <= 0) and (self.p2.y - other.p1.y >= 0)) or ((self.p1.y - other.p1.y >= 0) and (self.p2.y - other.p1.y <= 0)):
                        return Point(self.p1.x, other.p1.y)
                return None
            else:
                return None

class Wire:
    def __init__(self):
        self.lines = []
        self.origin = Point(1000000, 1000000)

    def add_line(self, l):
        self.lines.append(l)

wires = [Wire(),Wire()]
wires[0].add_line(Line(Point(1000000, 1000000),Point(1000000, 1000000)))
wires[1].add_line(Line(Point(1000000, 1000000),Point(1000000, 1000000)))

#print(wires_data)

for i, w in enumerate(wires_data):
    for j, d in enumerate(w):
        opcode = d[0]
        number = int(d[1::])
        anchor = wires[i].lines[-1].p2
        end_point = None
        if opcode == "U":
            end_point = Point(anchor.x, anchor.y + number)
        if opcode == "D":
            end_point = Point(anchor.x, anchor.y - number)
        if opcode == "R":
            end_point = Point(anchor.x + number, anchor.y)
        if opcode == "L":
            end_point = Point(anchor.x - number, anchor.y)

        wires[i].add_line(Line(anchor, end_point))

distances = []

for red in wires[0].lines[1::]:
    for blue in wires[1].lines[1::]:
        ins = red.get_intersection(blue)
        if ins is not None:
            dis = Point(1000000, 1000000).distance_from(ins)
            distances.append(dis)
            print("Distance: %i, point: %i, %i" % (dis, ins.x, ins.y))
distances.sort()
print(distances)
#print(wires[0].lines)


# p = [Point(2, 2), Point(10,2), Point(5,1), Point(5,10)]

# l1 = Line(p[0], p[1])

# l2 = Line(p[2], p[3])

# print("X: %i, Y: %i" % (l2.get_intersection(l1).x, l2.get_intersection(l1).y))

    
