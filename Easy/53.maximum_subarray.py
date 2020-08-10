# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #add previous number to current number if it was positive.
        #previous number will still be the same, so it wouldn't matter if it helped or not.
        #if current number was positive, it will be bigger by the prev. amount.
        #if current number was negative, then it wouldn't matter, bc max would choose prev number over current.
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
        
