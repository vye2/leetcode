# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
#
#
#
# Example 1:
#
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#
#
# Constraints:
#
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        #Traverse backwards, and then replace current number with previous max,
        #and calculate max for next iteration.
        prev = -1

        for i in range(len(arr)):
            arr[~i], prev = prev, max(prev, arr[~i])

        return arr
