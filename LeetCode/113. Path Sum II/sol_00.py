# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def is_none(node):
            return node == None
        def left(node):
            return node.left
        def right(node):
            return node.right
        def is_leaf(node):
            return left(node) == right(node) == None
        def value(node):
            return node.val
        
        
        def recurse(node, target, temp, history):
            if is_none(node):
                return history
            temp.append(value(node))
            if is_leaf(node) and value(node) == target:
                history.append(temp)
                return history
            
            target -= value(node)
            recurse(left(node), target, temp[::], history)
            recurse(right(node), target, temp[::], history)
            return history
        return recurse(root, targetSum, [], [])