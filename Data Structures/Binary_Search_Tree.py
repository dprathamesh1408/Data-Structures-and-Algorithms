'''
@Author: Prathamesh Deshpande
@Date:  2024-09-19
@Last Modified by: Prathamesh Deshpande
@Last Modified time: 2024-09-19
@Title : Python program to implement Binary Search Tree.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def insert(self, root, key):
        """
        Description:
            Insert a new node with the given key into the BST.
        
        Args:
            - root: 
                The root node of the BST.
            - key: 
                The value of the node to be inserted.
        
        Returns:
        -   The root node of the updated BST.
        """
         
        if root is None:
            return Node(key)
        
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        return root

    def inorder_traversal(self, root):
        """
        Description:
            Perform an inorder traversal of the BST.
        
        Args:
            - root: 
                The root node of the BST.
        
        Returns:
        -   None. Prints the nodes in inorder sequence.
        """
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)


def main():
     
    bst = BST()
    root = None

    nodes = [50, 30, 20, 40, 70, 60, 80]
    for node in nodes:
        root = bst.insert(root, node)

    print("Inorder traversal of the BST:")
    bst.inorder_traversal(root)


if __name__ == "__main__":
    main()
