with open("input.txt", "r") as file:
    lines = file.read().split("\n")
    data = []
    for b in lines:
        n = b.split(")")
        data.append((n[0], n[1]))

# print(data)


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
    


root = Body(None, "COM")

while len(data) > 0:
    for d in data:
        body = root.get_body_by_name(d[0])
        if body is not None:
            body.add_child(Body(body, d[1]))
            data.remove(d)

print(root.get_recursive_num_of_connectins())

# for d in data:
#     found = False
#     parent = d[0]
#     child = d[1]
#     for b in bodies:
#         node = b.get_body_by_name(parent)
#         if node is not None:
#             node.add_child(Body(node, child))
#         else:
#             created = Body(None, parent)
#             created.add_child(Body(created, child))
#             bodies.append(created)

# print(bodies)
