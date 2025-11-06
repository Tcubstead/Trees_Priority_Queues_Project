#Thomas Cubstead
#Trees_Priority_Queues_Project
#Binary_Tree_Project.py
#11/6/25
#

# stack.py
class Stack:
    """Stack implementation using Python list."""
    
    def __init__(self):
        """Create an empty stack."""
        self._items = []
    
    def is_empty(self):
        """Return True if stack is empty."""
        return len(self._items) == 0
    
    def push(self, item):
        """Add item to top of stack."""
        self._items.append(item)
    
    def pop(self):
        """Remove and return top item from stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def top(self):
        """Return top item without removing it."""
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._items[-1]
    
    def size(self):
        """Return number of items in stack."""
        return len(self._items)

class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

class BianaryExpressionTree:
    def __init__(self):
        self.root = None

    def is_empty(self) -> bool:
        return self.root is None

    def clear_tree(self):
        self.root = None

    def build_from_postfix(self, postfix: str):
        if not postfix or postfix.strip() == "":
            raise ValueError("Empty postfix expression")

        tokens = postfix.split()
        stack = Stack()
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in tokens:
                if stack.is_empty:
                    raise ValueError("stack is empty - insufficient operands")

                node = Node(token)

                if not stack.is_empty():
                    node.right = stack.top()
                    stack.pop()
                else:
                    raise ValueError("stack is empty - insufficient operands")

                if not stack.is_empty():
                    node.left = stack.top()
                    stack.pop()
                else:
                    raise ValueError("stack is empty - insufficient operands")

                stack.push(node)

            else:
                try:
                    float(token)
                    node = Node(token)
                    stack.push(node)
                except ValueError:
                    raise ValueError(f"unsupported token: '{token}'")

        if stack.is_empty():
            raise ValueError("invalid expression: no resulting tree")

        self.root = stack.top()
        stack.pop()

        if not stack.is_empty():
            raise ValueError(f"invalid expression: extra operands remaining in stack")