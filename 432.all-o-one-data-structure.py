#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (31.85%)
# Likes:    568
# Dislikes: 74
# Total Accepted:    30.2K
# Total Submissions: 94.6K
# Testcase Example:  '["AllOne","getMaxKey","getMinKey"]\n[[],[],[]]'
#
# Implement a data structure supporting the following operations:
# 
# 
# 
# Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by
# 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise
# decrements an existing key by 1. If the key does not exist, this function
# does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element
# exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element
# exists, return an empty string "".
# 
# 
# 
# 
# Challenge: Perform all these in O(1) time complexity.
# 
#

# @lc code=start
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_val = {}
        self.val_key = {}
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key_val:
            oldVal = self.key_val[key]
            self.key_val[key] += 1
            self.val_key[oldVal].remove(key)
            if not self.val_key[oldVal]:
                del self.val_key[oldVal]
        else:
            oldVal = 0
            self.key_val[key] = 1
        if oldVal+1 in self.val_key:
            self.val_key[oldVal+1].add(key)
        else:
            self.val_key[oldVal+1] = {key}
        
       


    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key_val: return 
        oldVal = self.key_val[key]
        self.key_val[key] -= 1
        self.val_key[oldVal].remove(key)
        if not self.val_key[oldVal]:
            del self.val_key[oldVal]
        if oldVal-1 == 0:
            del self.key_val[key]
        else:
            if oldVal-1 in self.val_key:
                self.val_key[oldVal-1].add(key)
            else:
                self.val_key[oldVal-1] = {key}

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.val_key:
            return ""
        maxVal = max(self.val_key.keys())
        res = self.val_key[maxVal].pop()
        self.val_key[maxVal].add(res)
        return res
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.val_key:
            return ""
        minVal = min(self.val_key.keys())
        res = self.val_key[minVal].pop()
        self.val_key[minVal].add(res)
        return res


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

