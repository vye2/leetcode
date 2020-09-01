# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #Hashtable

        D = defaultdict(int)

        for num in nums:
            D[num] += 1

        for i in D:
            if D[i] == 1:
                return i

        #Math
        #2∗(a+b+c)−(a+a+b+b+c)=c
        return 2 * sum(set(nums)) - sum(nums)

        #bit manipulation
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans
