#Thomas Cubstead
#Trees_Priority_Queues_Project
#Binary_Tree_Traversal_Project
#11/6/25
#

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

