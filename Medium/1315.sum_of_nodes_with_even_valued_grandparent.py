# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
#
# If there are no nodes with an even-valued grandparent, return 0.
#
#
#
# Example 1:
#
#
#
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
#
#
# Constraints:
#
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        #if current node is null, return
        #need to remember parent, as well as grandparent.
        #if current node's grandparent was even, add current val.
        #new parent is now root, new grandparent is now parent.


        runningSum = 0

        def helper(root, parent, grandparent):
            nonlocal runningSum

            if root==None:
                return 0

            if grandparent % 2 == 0:
                runningSum += root.val

            helper(root.left, root.val, parent)
            helper(root.right, root.val, parent)

        helper(root, 1, 1)
        return runningSum

            
