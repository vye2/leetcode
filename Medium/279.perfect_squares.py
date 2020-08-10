# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:
    def numSquares(self, n: int) -> int:

        #square root n, and then
        a = math.floor(math.sqrt(n))
        DP = []
        if a * a == n:
            return 1
        if n <= 3:
            return n


        for i in range(n+1):
            DP.append(i)
            j = 1
            while j * j <= i:
                DP[i] = min(DP[i], 1 + DP[i-j*j])
                j+=1

        return DP[n]
                
