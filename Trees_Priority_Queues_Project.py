#Thomas Cubstead
#Trees_Priority_Queues_Project
#Binary_Tree_Project.py
#11/6/25
#This program implements a binary expression tree that can build itself from a postfix expression

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

#class for the individual nodes of the binary expression tree
class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

#Binary Expression Tree class
class BinaryExpressionTree:
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
        stack = Stack()  # Use Stack class instead of Python list
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            # Check if token is an operator
            if token in operators:
                # Need two operands for binary operator
                if stack.is_empty():
                    raise ValueError("Stack is empty - insufficient operands")
                
                # Create operator node
                node = Node(token)
                
                # Pop right operand
                if not stack.is_empty():
                    node.right = stack.top()
                    stack.pop()
                else:
                    raise ValueError("Stack is empty - insufficient operands")
                
                # Pop left operand
                if not stack.is_empty():
                    node.left = stack.top()
                    stack.pop()
                else:
                    raise ValueError("Stack is empty - insufficient operands")
                
                # Push the new subtree back onto stack
                stack.push(node)
            else:
                # Token should be a number
                try:
                    # Validate it's a valid number
                    float(token)
                    # Create leaf node for operand
                    node = Node(token)
                    stack.push(node)
                except ValueError:
                    raise ValueError(f"Unsupported token: '{token}'")
        
        # After processing all tokens, should have exactly one tree
        if stack.is_empty():
            raise ValueError("Invalid expression: no result")
        
        # Pop the expression tree and store in root
        self.root = stack.top()
        stack.pop()
        
        # Check if there are unused tokens
        if not stack.is_empty():
            raise ValueError(f"Invalid expression: unused tokens left on stack")
    
    # Evaluate the expression tree and return the result
    def evaluate_tree(self) -> float:
        if self.is_empty():
            raise ValueError("can not ervaluate an empty tree")

        return self._evaluate(self.root)

    #recursively evaluate subtrees
    def _evaluate(self, p: Node) -> float:
        if p.left is None and p.right is None:
            return float(p.value)

        op = p.value
        x = self._evaluate(p.left)
        y = self._evaluate(p.right)

        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            if y == 0:
                raise ZeroDivisionError("division by zero")
            return x / y
    
    #return infix representation of the expression tree with parentheses
    def infix_traversal(self) -> str:
        if self.is_empty():
            raise ValueError("can not traverse an empty tree")

        result = []
        self._inorder(self.root, result)
        return ''.join(result)

    #helper for infix traversal
    def _inorder(self, node: Node, out: list):
        if node is None:
            return

        out.append('(')
        self._inorder(node.left, out)
        out.append(' ')
        out.append(node.value)
        out.append(' ')
        self._inorder(node.right, out)
        out.append(')')
    
    #return postfix representation of the expression tree
    def postfix_traversal(self) -> str:
        if self.is_empty():
            raise ValueError("can not traverse an empty tree")

        result = []
        self._postorder(self.root, result)
        return ' '.join(result)

    #helper for postfix traversal
    def _postorder(self, node: Node, out: list):
        if node is None:
            return

        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append(node.value)

def main():
# Test data from the Evaluating Expressions Project
    postfix_expressions = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]
    
    print("----- Binary Expression Tree -----")
    
    for postfix in postfix_expressions:
        tree = BinaryExpressionTree()
        
        try:
            # Build from postfix expression
            tree.build_from_postfix(postfix)
            
            # Get infix and postfix representations
            infix = tree.infix_traversal()
            postfix_result = tree.postfix_traversal()
            
            # Evaluate the expression
            result = tree.evaluate_tree()
            
            # Display results
            print(f"Infix Expression: {infix}")
            print(f"Postfix Expression: {postfix_result}")
            print(f"Evaluated Result: {result}")
            print()
            
        except Exception as e:
            print(f"Error processing '{postfix}': {e}")
            print()


if __name__ == "__main__":
    main()