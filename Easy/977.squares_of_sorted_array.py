# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
#
#
#
# Example 1:
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Note:
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        #Use two pointers to compare the absolute values of the negative numbers w the positive.

        start = 0
        end = len(A) - 1

        if (A[start] < 0 and A[end] < 0) or (A[start] > 0 and A[end] > 0):
            return [i*i for i in A]

        ans = []

        while start <= end:
            if (A[end]) >= abs(A[start]):
                ans.append((A[end] * A[end]))
                end -= 1

            elif abs(A[start]) > (A[end]):
                ans.append((A[start] * A[start]))
                start +=1

        return reversed(ans)
