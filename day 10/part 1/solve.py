import json

with open("C:\\Users\\gabirat\\Desktop\\Python\\adventofcode\\day 10\\part 1\\test_input.txt", "r") as file:
    data = [val for val in file.read().split("\n")]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @staticmethod
    def distance_sq(p1, p2):
        return (p2.x - p1.x)**2 + (p2.y - p1.y)**2

class Line:
    def __init__(self, a=None, b=None, vertical=False, x=None):
        self.a = a
        self.b = b
        self.x = x
        self.vertical = vertical

    def get_y(self, x):
        return self.a * x + self.b

    def has_point(self, p1):
        if self.vertical:
            return p1.x == self.x
        else:
            return self.get_y(p1.x) == p1.y

    @staticmethod
    def from_points(p1, p2):
        run = (p2.x - p1.x)
        if run != 0:
            a = (p2.y - p1.y)/run
        else:
            return Line(vertical=True, x=p1.x)

        b = p1.y - a * p1.x
        return Line(a, b)


class Asteroid(Point):
    def __init__(self, x, y):
        super().__init__(x,y)


asteroids = []
for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char == "#":
            asteroids.append(Asteroid(j, i))

def sees(a1, a2):
    line_of_sight = Line.from_points(a1, a2)
    d = Point.distance_sq(a1, a2)
    for a3 in asteroids:
        if a3 is a1 or a3 is a2:
            continue
        if line_of_sight.has_point(a3) and Point.distance_sq(a3, a1) < d and Point.distance_sq(a3, a2) < d:
            return False
    return True

def monitoring_station_range(a):
    r = 0
    for a1 in asteroids:
        if a1 is a:
            continue
        if sees(a, a1):
            r += 1
    return r

ranges = []

for ast in asteroids:
    ranges.append( (monitoring_station_range(ast), ast) )

ranges.sort(key = lambda i: i[0])

for r in ranges:
    print("Best: %i at X: %i, Y: %i" % (r[0], r[1].x, r[1].y))
            