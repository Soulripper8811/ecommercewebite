class Node:
    def __init__(self, name, heuristic=0):
        self.name = name
        self.heuristic = heuristic
        self.children = []

    def add_child(self, node, is_and=True):
        self.children.append((node, is_and))

def ao_star(node, path=[]):
    if not node.children:  
        return node.heuristic, path + [node.name]

    min_cost = float('inf')
    optimal_path = []

    for child, is_and in node.children:
        if is_and: 
            total_cost, sub_path = 0, []
            for c, _ in node.children:
                cost, child_path = ao_star(c, path + [node.name])
                total_cost += cost
                sub_path.extend(child_path)
        else:
            total_cost, sub_path = ao_star(child, path + [node.name])

        if total_cost < min_cost:
            min_cost = total_cost
            optimal_path = sub_path

    node.heuristic = min_cost
    return min_cost, optimal_path


root = Node("Start")
n1 = Node("A", heuristic=5)
n2 = Node("B", heuristic=3)
n3 = Node("C", heuristic=2)

root.add_child(n1, is_and=True)  
root.add_child(n2, is_and=False) 
n1.add_child(n3, is_and=False)

cost, path = ao_star(root)
print(f"Optimal Cost: {cost}")
print(f"Optimal Path: {' -> '.join(path)}")
