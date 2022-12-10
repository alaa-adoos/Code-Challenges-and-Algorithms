class Tree :
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None


    def __str__(self,node):
        self.print_Tree(node)
        return self.tree

    def print_Tree(self,node):
        """
        print nodes of tree 

        Args:
            node

        Returns:
            Void
        """
        if node is None:
            return None
        if node is not None:
            self.tree+=f'{node.value} ,'
        if node.left is not None:
            self.print_Tree(node.left)
        if node.right is not None:  
            self.print_Tree(node.right)


   
def two_sum_bst(root, k):
    """_summary_
      to detrimne if the binry tree has two elements that their summation  is given integer 

    Args:
        root (ListNode): binary search tree
        k (integer)

    Returns:
        Boolean
    """
    values = set()
    def Target(root):
        if not root:
            return False
        if k - root.value in values:
            return True
        values.add(root.value)
        return Target(root.left) or Target(root.right)
    return Target(root)
