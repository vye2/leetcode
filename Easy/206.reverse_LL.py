# 206. Reverse Linked List
# Easy
#
# 4755
#
# 91
#
# Add to List
#
# Share
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #base case: if current node is None, then return accumulated.
        #recursion approach.
        def helper(head, prev=None):
            if head == None:
                return prev

            temp = head.next
            head.next = prev
            return helper(temp, head)

        return helper(head)

        #iter approach.
        ans = None
        while head:
            curr = head
            head = head.next
            curr.next = ans
            ans = curr
        return ans
