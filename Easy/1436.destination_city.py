# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
#
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
#
#
#
# Example 1:
#
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo"
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
# Example 2:
#
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are:
# "D" -> "B" -> "C" -> "A".
# "B" -> "C" -> "A".
# "C" -> "A".
# "A".
# Clearly the destination city is "A".
# Example 3:
#
# Input: paths = [["A","Z"]]
# Output: "Z"
#
#
# Constraints:
#
# 1 <= paths.length <= 100
# paths[i].length == 2
# 1 <= cityAi.length, cityBi.length <= 10
# cityAi != cityBi
# All strings consist of lowercase and uppercase English letters and the space character.


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #basically find a cityB such that for all paths, cityA!=B
        first, second = [c[0] for c in paths], [c[1] for c in paths]
        return  (set(second) - set(first)).pop()

        # A, B, C, D
        # B, C, D, E


        # D = {}
        #
        # for i in range(len(paths)):
        #     if paths[i][0] not in D:
        #         D[paths[i][0]] = 1
        #     else:
        #         D[paths[i][0]] += 1
        #
        #     if paths[i][1] not in D:
        #         D[paths[i][1]] = -1
        #     else:
        #         D[paths[i][1]] += -1
        #
        #
        # for k, v in D.items():
        #     if v == int(-1):
        #         return k
        # return
