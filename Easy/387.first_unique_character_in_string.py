# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
# Note: You may assume the string contains only lowercase English letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:

        D = defaultdict(int)

        for i in s:
            D[i] += 1


        for i, ch in enumerate(s):
            if D[ch] == 1:
                return i

        return -1


        #Faster solution cuz less items to traverse

        D = defaultdict(int)

        for i in s:
            D[i] += 1


        first = -1
        for i, (k, v) in enumerate(D.items()):

            if first == -1 and v == 1:
                first = s.index(k)

        return first
