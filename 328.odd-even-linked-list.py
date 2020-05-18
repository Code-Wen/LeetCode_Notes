#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (53.13%)
# Likes:    1562
# Dislikes: 283
# Total Accepted:    238.8K
# Total Submissions: 441.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# 
# 
# Example 2:
# 
# 
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# 
# 
# Note:
# 
# 
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        n = 1
        oddHead, evenHead = ListNode(), ListNode()
        node, oddNode, evenNode = head, oddHead, evenHead
        while node:
            if n%2:
                oddNode.next = node
                oddNode = node
            else:
                evenNode.next = node
                evenNode = node
            n += 1    
            temp = node.next
            node.next = None
            node = temp
        oddNode.next = evenHead.next
        return oddHead.next
# @lc code=end

