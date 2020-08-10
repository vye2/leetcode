# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# Note:
# The size of the given array will be in the range [1,1000].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        #Recursive solution
        def helper(numss, start, end):
            if start > end:
                return None

            maxVal = max(numss[start:end+1])
            maxIndexOfSubList = numss.index(maxVal)

            print(maxIndexOfSubList)

            root = TreeNode(maxVal)

            root.left = helper(numss, start, maxIndexOfSubList-1)
            root.right = helper(numss, maxIndexOfSubList+1, end)

            return root


        return helper(nums, 0, len(nums)-1)


        #Iterative solution
        stack = []
        for num in nums:

            root = TreeNode(num)

            if len(stack)==0:
                stack.append(root)

            elif stack[-1].val > num:
                stack[-1].right = root

            else:
                while stack and stack[-1].val < num:
                    root.left = stack.pop()
                if stack:
                    stack[-1].right = root

            stack.append(root)
        return stack[0]
