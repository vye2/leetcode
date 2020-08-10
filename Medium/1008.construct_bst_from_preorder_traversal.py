# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
#
# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.
#
# Example 1:
#
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
#
#
#
# Constraints:
#
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# The values of preorder are distinct.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
                8
              /   \
             5    10
            / \     \
           1   7    12
        """
        #first element is root, with bounds (min, max)
        #if preorder[i] is < root and > root_left_bound(or min), then root.left = preorder[i], with bounds (root_left_bound, root-1)
        #if preorder[i] is > root and < root_right_bound(or max), then root.right = preorder[i], with bounds (root+1, root_right_bound)

        def helper(root, val):
            if root is None: #that means we have arrived
                 return TreeNode(val)
            if val < root.val:
                root.left = helper(root.left, val)
            else:
                root.right = helper(root.right, val)

            return root

        root = None
        for i in range(len(preorder)):
            root = helper(root, preorder[i])
        return root



        #lee215 solution
        # Give the function a bound the maximum number it will handle.
        # The left recursion will take the elements smaller than node.val
        # The right recursion will take the remaining elements smaller than bound
        #
        # Complexity
        # bstFromPreorder is called exactly N times.
        # It's same as a preorder traversal.
        # Time O(N)
        # Space O(H)
        i = 0
        def bstFromPreorder(self, A, bound=float('inf')):
            if self.i == len(A) or A[self.i] > bound:
                return None
            root = TreeNode(A[self.i])
            self.i += 1
            root.left = self.bstFromPreorder(A, root.val)
            root.right = self.bstFromPreorder(A, bound)
            return root
