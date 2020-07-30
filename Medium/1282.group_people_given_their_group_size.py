# There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n
# telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.
# You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution.

# Example1
# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]
# Explanation:
# Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].


# Example2
# Input: groupSizes = [2,1,3,3,3,2]
# Output: [[1],[0,5],[2,3,4]]


# Constraint
# groupSizes.length == n
# 1 <= n <= 500
# 1 <= groupSizes[i] <= n


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        D = {}
        for personID, groupSize in enumerate(groupSizes):
            #loop through, make empty arr size of groupSizes[personID] if it does not exist in hashmap.
            #if it does exist, then add to that array.
            #if array is full, then add that array to ans, and remove that key
            #temp = groupSizes[personID] in D ? D[groupSizes[personID]] : D[group]
            if groupSize not in D:
                D[groupSize] = []

            D[groupSize].append(personID)

            if len(D[groupSize]) == groupSize:
                ans.append(D[groupSize])
                D[groupSize] = []

        return ans
