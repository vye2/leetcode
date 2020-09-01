# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def dfs(left, right, S):

            if left == 0 and right == 0:
                ans.append(S)
                return

            if left > 0:
                dfs(left-1, right, S+'(')
            if right > left:
                dfs(left, right-1, S+')')

        dfs(n, n, '')


        return ans
