from typing import List

class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
    def distance(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
    def __hash__(self):
        return hash((self.x, self.y, self.z))

class CircuitItem(Point):
    def __init__(self, x: int, y: int, z: int):
        super().__init__(x, y, z)
        self.connections: List[CircuitItem] = []
    def connect(self, other: "CircuitItem"):
        if other not in self.connections:
            self.connections.append(other)
            other.connections.append(self)
    # Recursively check connections
    def is_connected(self, other: "CircuitItem") -> bool:
        visited = set()
        def dfs(item: "CircuitItem") -> bool:
            if item == other:
                return True
            visited.add(item)
            for conn in item.connections:
                if conn not in visited:
                    if dfs(conn):
                        return True
            return False
        return dfs(self)

def parse_input(path: str) -> List[CircuitItem]:
    with open(path, 'r') as f:
        return [CircuitItem(*map(int, line.strip().split(','))) for line in f.readlines()]



if __name__ == "__main__":
    circuit_items = parse_input("2025/8/input.txt")
    distances = []
    for i in range(len(circuit_items)):
        for j in range(len(circuit_items)):
            if i == j:
                break
            distance = circuit_items[i].distance(circuit_items[j])
            distances.append((circuit_items[i], circuit_items[j], distance))
    distances.sort(key=lambda x: x[2])
    # Iterate overr first 10 items
    for item1, item2, dist in distances[:1000]:
        if item1.is_connected(item2):
            continue
        item1.connect(item2)

    tree_sizes = []
    # Display individual trees
    visited = set()
    for item in circuit_items:
        if item in visited:
            continue
        stack = [item]
        tree = []
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            tree.append(current)
            for conn in current.connections:
                if conn not in visited:
                    stack.append(conn)
        tree_sizes.append(len(tree))

    tree_sizes.sort(reverse=True)
    print("Solution:", tree_sizes[0] * tree_sizes[1] * tree_sizes[2])