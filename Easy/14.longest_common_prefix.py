# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ''

        if not strs:
            return ''

        for i in range(len(min(strs, key=len))):
            c = strs[0][i]
            if all(st[i] == c for st in strs):
                prefix += c
            else:
                break
        return prefix
