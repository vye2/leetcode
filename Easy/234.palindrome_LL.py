# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        q = []

        while head:
            q.append(head.val)
            head = head.next

        i, j = 0, len(q)-1

        while i < j:
            if q[i] != q[j]:
                return False
            i+=1
            j-=1

        return True
        # reverse a list like this:
        # return q == q[::-1]

        # Reversing first half and checking if equals second.

        if head == None or not head.next:
            return True

        rev = None
        fast = slow = head


        while fast and fast.next:
            fast = fast.next.next
            temp = rev
            rev = slow
            slow = slow.next
            rev.next = temp

        #if odd number length, then skip middle check.
        if fast:
            slow = slow.next


        # while rev:
        #     if rev.val != slow.val:
        #         return False
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev
