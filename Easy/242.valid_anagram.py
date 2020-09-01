# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        if len(s) != len(t):
            return False

        D1, D2 = defaultdict(int), defaultdict(int)

        for l1, l2 in zip(s, t):
            D1[l1] += 1
            D2[l2] += 1

        return D1 == D2

            
