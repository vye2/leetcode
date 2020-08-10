# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                count+=1
        nums+=([0]*count)

        #simplified version:

        count = nums.count(0)
        nums[:] = [i for i in nums if i!=0]
        nums+=([0]*count)
