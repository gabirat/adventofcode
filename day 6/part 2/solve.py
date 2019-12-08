import pickle
import sys

sys.setrecursionlimit(3000)

# with open("input.txt", "r") as file:
#     lines = file.read().split("\n")
#     data = []
#     for b in lines:
#         n = b.split(")")
#         data.append((n[0], n[1]))

class Body:
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, ch):
        self.children.append(ch)

    def get_body_by_name(self, name):
        if self.name == name:
            return self
        for c in self.children:
            n = c.get_body_by_name(name)
            if n is not None:
                return n
        return None

    def get_num_of_connections(self):
        if len(self.children) == 0:
            return 0
        else:
            cons = len(self.children)
            for c in self.children:
                cons += c.get_num_of_connections()
            return cons

    def get_recursive_num_of_connectins(self):
        cons = self.get_num_of_connections()
        for c in self.children:
            cons += c.get_recursive_num_of_connectins()
        return cons

    def get_dist_to_child(self, name, inc=-1):
        if self.name == name:
            return inc
        for c in self.children:
            n = c.get_dist_to_child(name, inc+1)
            if n is not None:
                return n
        return None

with open("root.orbits", "rb") as root_orbits_file:
    root = pickle.load(root_orbits_file)

orbits_away = 0

me = root.get_body_by_name("YOU")

while me.parent.get_body_by_name("SAN") is None:
    orbits_away += 1
    me.parent.parent.add_child(me)
    me.parent.children.remove(me)
    me.parent = me.parent.parent

orbits_away += me.parent.get_dist_to_child("SAN")

print(orbits_away)
