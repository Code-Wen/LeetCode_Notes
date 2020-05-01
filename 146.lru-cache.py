#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (30.78%)
# Likes:    5099
# Dislikes: 227
# Total Accepted:    482.6K
# Total Submissions: 1.6M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.history = {}
        self.time = 0
        self.last = 0

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        
        val, lastTime = self.cache[key]
        del self.history[lastTime]
        self.cache[key][1] = self.time
        self.history[self.time] = key
        while self.last not in self.history:
            self.last += 1
        self.time += 1
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            lastTime = self.cache[key][1]
            del self.history[lastTime]
        
        elif len(self.cache) == self.cap:
            toDrop =  self.history[self.last]
            del self.history[self.last]
            del self.cache[toDrop]
            
        self.history[self.time] = key
        while self.last not in self.history :
                self.last += 1
        self.cache[key] =  [value, self.time]
        self.time += 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

