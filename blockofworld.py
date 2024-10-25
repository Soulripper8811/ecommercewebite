class BlockWorld:
    def __init__(self, num_blocks):
        # Initialize each block on its own stack
        self.stacks = [[i] for i in range(num_blocks)]
    
    def __str__(self):
        # Represent the world state as a string
        return '\n'.join(f'{i}: {stack}' for i, stack in enumerate(self.stacks))
    
    def move_onto(self, a, b):
        self.clear_above(a)
        self.clear_above(b)
        self.stacks[b].append(a)
    
    def move_over(self, a, b):
        self.clear_above(a)
        self.stacks[b].append(a)
    
    def pile_onto(self, a, b):
        self.clear_above(b)
        pile = self.remove_pile(a)
        self.stacks[b].extend(pile)
    
    def pile_over(self, a, b):
        pile = self.remove_pile(a)
        self.stacks[b].extend(pile)
    
    def clear_above(self, block):
        stack = self.find_stack(block)
        index = stack.index(block)
        for b in stack[index + 1:]:
            self.stacks[b].append(b)
        del stack[index + 1:]
    
    def find_stack(self, block):
        for stack in self.stacks:
            if block in stack:
                return stack
        return None
    
    def remove_pile(self, block):
        stack = self.find_stack(block)
        index = stack.index(block)
        pile = stack[index:]
        del stack[index:]
        return pile

# Example usage:
world = BlockWorld(5)
print("Initial State:")
print(world)

# Move block 1 onto block 3
world.move_onto(1, 3)
print("\nAfter moving block 1 onto block 3:")
print(world)

# Move block 2 over block 4
world.move_over(2, 4)
print("\nAfter moving block 2 over block 4:")
print(world)

# Pile block 0 and block 4 onto block 3
world.pile_onto(0, 3)
print("\nAfter piling block 0 and block 4 onto block 3:")
print(world)

# Pile block 3 and block 4 over block 1
world.pile_over(3, 1)
print("\nAfter piling block 3 and block 4 over block 1:")
print(world)


