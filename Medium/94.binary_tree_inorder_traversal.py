# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

#         ans = []

#         def helper(root):
#             if root != None:
#                 if root.left: Not needed
#                     helper(root.left)
#                 ans.append(root.val)
#                 if root.right: Not needed
#                     helper(root.right)


#         helper(root)
#         return ans

        stk = []
        ans = []
        # curr = root

        while curr or len(stk) > 0:

            if curr:
                stk.append(curr)
                curr = curr.left
            else:
                curr = stk.pop()
                ans.append(curr.val)
                curr = curr.right

        return ans
