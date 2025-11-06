#Thomas Cubstead
#Trees_Priority_Queues_Project
#Binary_Tree_Traversal_Project
#11/6/25
#This program provides solutions to binary tree traversal problems and reconstructs binary trees from given traversals

#class for the individual nodes of the binary expression tree
class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

#Binary Tree class with traversal and reconstruction methods
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    # Traversal Methods
    def preorder_traversal(self):
        """Preorder: Root → Left → Right"""
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
    
    def inorder_traversal(self):
        """Inorder: Left → Root → Right"""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
    
    def postorder_traversal(self):
        """Postorder: Left → Right → Root"""
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)
    
    # Tree Reconstruction Methods
    @staticmethod
    def from_preorder_inorder(preorder, inorder):
        """Reconstruct tree from preorder and inorder traversals."""
        if not preorder or not inorder:
            return BinaryTree(None)
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # First element in preorder is root
            root_val = preorder[pre_start]
            root = Node(root_val)
            
            # Find root in inorder
            root_idx = inorder.index(root_val)
            
            # Number of nodes in left subtree
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, 
                            in_start, root_idx - 1)
            root.right = build(pre_start + left_size + 1, pre_end, 
                             root_idx + 1, in_end)
            
            return root
        
        root = build(0, len(preorder) - 1, 0, len(inorder) - 1)
        return BinaryTree(root)
    
    @staticmethod
    def from_postorder_inorder(postorder, inorder):
        """Reconstruct tree from postorder and inorder traversals."""
        if not postorder or not inorder:
            return BinaryTree(None)
        
        def build(post_start, post_end, in_start, in_end):
            if post_start > post_end or in_start > in_end:
                return None
            
            # Last element in postorder is root
            root_val = postorder[post_end]
            root = Node(root_val)
            
            # Find root in inorder
            root_idx = inorder.index(root_val)
            
            # Number of nodes in left subtree
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(post_start, post_start + left_size - 1, 
                            in_start, root_idx - 1)
            root.right = build(post_start + left_size, post_end - 1, 
                             root_idx + 1, in_end)
            
            return root
        
        root = build(0, len(postorder) - 1, 0, len(inorder) - 1)
        return BinaryTree(root)
    
    def display_tree(self):
        """Display tree structure in a readable format."""
        if not self.root:
            return "Empty tree"
        
        lines = []
        self._build_tree_string(self.root, 0, lines)
        return '\n'.join(lines)
    
    def _build_tree_string(self, node, level, lines):
        """Helper to build string representation of tree."""
        if node:
            self._build_tree_string(node.right, level + 1, lines)
            lines.append('    ' * level + str(node.value))
            self._build_tree_string(node.left, level + 1, lines)

def build_problem_tree():
    """Build the tree from problems 1-3:
           8
          / \\
         3   10
        / \\   \\
       1   6   14
          / \\  /
         4   7 13
    """
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    
    root.left.left = Node(1)
    root.left.right = Node(6)
    
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    
    return BinaryTree(root)


def main():
    print("=" * 60)
    print("BINARY TREE TRAVERSAL SOLUTIONS")
    print("=" * 60)
    
    # Problems 1-3: Traversals on given tree
    print("\n--- Problems 1-3: Tree Structure ---")
    print("""
           8
          / \\
         3   10
        / \\   \\
       1   6   14
          / \\  /
         4   7 13
    """)
    
    tree = build_problem_tree()
    
    print("\n1. PREORDER TRAVERSAL (Root → Left → Right):")
    preorder = tree.preorder_traversal()
    print(f"   Solution: {' '.join(map(str, preorder))}")
    
    print("\n2. INORDER TRAVERSAL (Left → Root → Right):")
    inorder = tree.inorder_traversal()
    print(f"   Solution: {' '.join(map(str, inorder))}")
    
    print("\n3. POSTORDER TRAVERSAL (Left → Right → Root):")
    postorder = tree.postorder_traversal()
    print(f"   Solution: {' '.join(map(str, postorder))}")
    
    # Problem 4: Reconstruct from preorder and inorder
    print("\n" + "=" * 60)
    print("4. RECONSTRUCT FROM PREORDER AND INORDER")
    print("=" * 60)
    print("Given:")
    print("   Preorder:  Q W E R T Y U I")
    print("   Inorder:   E W T R Q Y U I")
    
    preorder_4 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I']
    inorder_4 = ['E', 'W', 'T', 'R', 'Q', 'Y', 'U', 'I']
    
    tree_4 = BinaryTree.from_preorder_inorder(preorder_4, inorder_4)
    
    print("\nReconstructed Tree:")
    print(tree_4.display_tree())
    
    print("\nVerification:")
    print(f"   Preorder:  {' '.join(tree_4.preorder_traversal())}")
    print(f"   Inorder:   {' '.join(tree_4.inorder_traversal())}")
    print(f"   Postorder: {' '.join(tree_4.postorder_traversal())}")
    
    # Problem 5: Reconstruct from postorder and inorder
    print("\n" + "=" * 60)
    print("5. RECONSTRUCT FROM POSTORDER AND INORDER")
    print("=" * 60)
    print("Given:")
    print("   Postorder: J I L M N K H")
    print("   Inorder:   J I H L K M N")
    
    postorder_5 = ['J', 'I', 'L', 'M', 'N', 'K', 'H']
    inorder_5 = ['J', 'I', 'H', 'L', 'K', 'M', 'N']
    
    tree_5 = BinaryTree.from_postorder_inorder(postorder_5, inorder_5)
    
    print("\nReconstructed Tree:")
    print(tree_5.display_tree())
    
    print("\nVerification:")
    print(f"   Preorder:  {' '.join(tree_5.preorder_traversal())}")
    print(f"   Inorder:   {' '.join(tree_5.inorder_traversal())}")
    print(f"   Postorder: {' '.join(tree_5.postorder_traversal())}")
    
    print("\n" + "=" * 60)
    print("SOLUTIONS SUMMARY")
    print("=" * 60)
    print("\n1. Preorder:  8 3 1 6 4 7 10 14 13")
    print("2. Inorder:   1 3 4 6 7 8 10 13 14")
    print("3. Postorder: 1 4 7 6 3 13 14 10 8")
    print("\n4. Tree from Preorder + Inorder:")
    print("       Q")
    print("      / \\")
    print("     W   Y")
    print("    / \\   \\")
    print("   E   R   U")
    print("        \\   \\")
    print("         T   I")
    print("\n5. Tree from Postorder + Inorder:")
    print("       H")
    print("      / \\")
    print("     I   K")
    print("    /   / \\")
    print("   J   L   N")
    print("            \\")
    print("             M")
    print("=" * 60)


if __name__ == "__main__":
    main()