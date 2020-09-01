# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
# Follow up: Solve it both recursively and iteratively.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        #recursive solution
        def helper(t1, t2):


            if not t1 and not t2:
                return True

            if not t1 or not t2:
                return False

            return ((t1.val == t2.val) and helper(t1.left, t2.right) and helper(t1.right, t2.left))


        return helper(root, root)


        #iterative solution
        Q = []

        Q.append(root)
        Q.append(root)

        while Q:

            t1 = Q.pop(0)
            t2 = Q.pop(0)

            if not t1 and not t2:
                continue

            if not t1 or not t2:
                return False

            if t1.val != t2.val:
                return False

            Q.append(t1.left)
            Q.append(t2.right)

            Q.append(t2.left)
            Q.append(t1.right)

        return True


        
