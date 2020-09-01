# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.


class Solution:
    def trailingZeroes(self, n: int) -> int:

        #To make 0s, you need 10s, which needs 5 and 2s.
        #There will always be more 2s than 5s because 2 is a smaller prime factor.
        #Sum the factors of 5's.


        # 34 33 32 31 30   25   20   15   10   5

        #125..

#         30 / 5 =6
#         30 / 25 = 1

#         125/5 = 25
#         125/25 = 5
#         125/125 = 1

        total = 0
        quint = 5
        while quint <= n:
            total += (n//quint)
            quint *=5

        return total
            
