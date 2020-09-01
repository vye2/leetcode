# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
#         perm = [][]

#         [1,2,3,4]

#         [1]          [2]           [3]    [4]
#         [2]   [3][4]    [1][3][4]
#         [3]

#         n = len(nums)
        ans = []

        def dfs(nums, perm):

            nonlocal ans
            if not nums:
                ans.append(perm)
                return

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], perm+[nums[i]])


        dfs(nums, [])
        return ans

            
