from collections import deque
class TreeNode(object):
    """
    class to bulid a tree 

    Args:
        object 
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.stack = []
    def buildTree(self, preorder, inorder):
        '''
        to get the input arrays and send to the  buildTree2 function
        '''
        preorder = deque(preorder)
        return self.buildTree2(preorder, inorder)

    def buildTree2(self, preorder, inorder):
        '''
        check the main root from the tow arrays
        '''
        if not inorder:  # empty list
            return None

        ind_root_val = inorder.index(preorder.popleft())
        root_node = TreeNode(inorder[ind_root_val])
        root_node.left  = self.buildTree2(preorder, inorder[:ind_root_val])
        root_node.right = self.buildTree2(preorder, inorder[ind_root_val + 1:])

        return root_node.val

    def findTree(self, preorder, inorder):
        '''
        build the tree body
        '''
        newtree = []
        if len(preorder) == 1 and len(inorder)==1:
            if preorder[0] == inorder[0]:
                return preorder
        if len(preorder) == 2 or len(preorder) == 3:
             return preorder
        if len(preorder) == 4:
            self.stack.append(preorder[0])
            inorder.remove(preorder[0])
            self.stack.append(preorder[1])
            inorder.remove(preorder[1])
            
            if preorder[2] != inorder[0]:
                self.stack.append(preorder[2])
                self.stack.append("null")
                self.stack.append("null")
                self.stack.append(preorder[3])
                self.stack.append("null")
                newtree = self.stack
                self.stack =[]
                return newtree
            if preorder[2] == inorder[0]:
                self.stack.append(preorder[3])
                self.stack.append(preorder[2])
                self.stack.append("null")
                self.stack.append("null")
                self.stack.append("null")
                newtree = self.stack
                return newtree
        
        if len(preorder) == 5:
            self.stack.append(preorder[0])
            inorder.remove(preorder[0])
            self.stack.append(preorder[1])
            inorder.remove(preorder[1])
            
            if preorder[2] != inorder[2]:
                self.stack.append(preorder[2])
                self.stack.append("null")
                self.stack.append("null")
                self.stack.append(preorder[3])
                self.stack.append(preorder[4])
                newtree = self.stack
                self.stack =[]
                return newtree
           
        #self.stack.append(preorder[0])
        #inorder.remove(preorder[0])
        #return inorder
    

test = TreeNode()
print(test.buildTree([3,9,20,15,7],[9,3,15,20,7]))
print(test.findTree([3,9,20,15,7],[9,3,15,20,7]))

print(test.buildTree([1],[1]))
print(test.findTree([1],[1]))
print(test.buildTree([1,2,3,4],[2,1,4,3]))
print(test.findTree([1,2,3,4],[2,1,4,3]))

print(test.buildTree([1,2,3],[2,1,3]))
print(test.findTree([1,2,3],[2,1,3]))

print(test.buildTree([3,9,4,10,20,15,7],[9,4,10,3,15,20,7]))
print(test.findTree([3,9,4,10,20,15,7],[9,4,10,3,15,20,7]))