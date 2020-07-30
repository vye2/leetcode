# Given a binary tree, return the sum of values of its deepest leaves.
#
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
#
#
# Constraints:
#
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.

        #need to keep track of depth.
        #if route has left = null and right = null,
        #save its value and its depth
        #upon discovery of a new max, replace max var.


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        #need to keep track of depth.
        #if route has left = null and right = null,
        #save its value and its depth
        #upon discovery of a new max, replace max var.

        depthMaxSoFar = 0;
        maxSum = 0;

        def deepest(root, depth):
            nonlocal maxSum
            nonlocal depthMaxSoFar

            if root==None:
                return
            if depth > depthMaxSoFar:
                depthMaxSoFar = depth
                maxSum = root.val

            elif depth == depthMaxSoFar:
                maxSum += root.val

            deepest(root.left, depth+1)
            deepest(root.right, depth+1)

        deepest(root, 0)
        return maxSum
