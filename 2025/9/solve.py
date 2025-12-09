from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    def distance(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    def __hash__(self):
        return hash((self.x, self.y))
    def area_between(self, other: "Point") -> float:
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)

def parse_input(path: str) -> List[Point]:
    with open(path, 'r') as f:
        return [Point(*map(int, line.strip().split(','))) for line in f.readlines()]



if __name__ == "__main__":
    points = parse_input("2025/9/input.txt")
    areas = []
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                break
            area = points[i].area_between(points[j])
            areas.append((points[i], points[j], area))
    areas.sort(key=lambda x: x[2], reverse=True)
    print(areas[0])
