# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
#
# Example 1:
#
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
#
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Notes:
#
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # [1,1,0],  [0,1,1]
        # [1,0,1],  [1,0,1]
        # [0,0,0],  [0,0,0]
        # In order to inverse a 1 to 0 and 0 to 1, do XOR with 1.
        # Or do 1 - x.

        for r in range(len(A)):
            for c in range((len(A[0])+1)//2):
                temp = A[r][c]
                A[r][c] = (A[r][~c] ^ 1)
                A[r][~c] = (temp ^ 1)

        return A
