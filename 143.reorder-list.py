#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (37.24%)
# Likes:    2179
# Dislikes: 122
# Total Accepted:    252.2K
# Total Submissions: 665.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        def findMid(head):
            """
            Find the middle node for a singly linked list.
            If there are even number of nodes, return the second mid node
            """
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        def reverse(head):
            """
            Reverse a singly linked list
            """
            prev, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            return prev
        
        def combine(firstHalf, secondHalf):
            """
            Combine two halves in a zigzag way
            """
            n1, n2 = firstHalf, secondHalf
            while n2.next:
                tmp1, tmp2 = n1.next, n2.next
                n1.next = n2
                n2.next = tmp1
                n1, n2 = tmp1, tmp2
            return firstHalf
        
        mid = findMid(head)
        secondHalf = reverse(mid)
        combine(head, secondHalf)

# @lc code=end

