#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (40.51%)
# Likes:    1905
# Dislikes: 347
# Total Accepted:    251.4K
# Total Submissions: 619.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        mid = head
        newHead, start = self.reverse(head, k)
        while start:
            nextMid = start
            head, start = self.reverse(start, k)
            mid.next = head
            mid = nextMid
        return newHead
            
        
    
    def reverse(self, head, k):
        """
        Reverse the first k nodes only if at least k nodes are present.
        Return the heads of the two parts.
        """
        # Check length >= k or not.
        length, node = 0, head
        while node and length < k:
            length += 1
            node = node.next
        if length < k: return head, None
        
        # Reverse if at least k nodes.
        cnt, node, prev = 0, head, None
        while cnt < k and node:
            nxt = node.next
            node.next = prev
            prev, node = node, nxt
            cnt += 1
        
        return prev, node
# @lc code=end

