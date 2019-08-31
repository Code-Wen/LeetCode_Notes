---
title: "Leetcode Algorithm Questions in Python 3"
excerpt: "Algorithmic thinking is a crucial component in every profession that involves coding, including data science. Here I'm documenting my solutions to algorithm questions on Leetcode, in hope that it would be of help to anyone interested."
collection: projects
---

## 38. Count and Say

[Link to the problem](https://leetcode.com/problems/count-and-say/)

**Analysis:**  
1. This is an inductive process. The *(k+1)*th reading depends on the *k*th reading.  
2. The starting point of the induction is the first reading, which we set as `seq="1"`.  
3. We need to recursively update `seq` *n-1* times.  
4. For each update, we use `list` to record the list of letters in the previoius `seq`. Starting with the first element `a=list[0]`, we count how many times `a` appears in the head of `list`, and record the number by `l`. In the process we also remove `a` in the head of `list`. Then we record the str `str(l)+a` in the list `stack`. Continue until we exhaust `list`, that is, when the length of `list` becomes 0.  In the last step we concatenate the strings in `stack` to form the new `seq`.   
5. Return `seq` which is the *n*th reading.

```
class Solution:
    def countAndSay(self, n: int) -> str:
        
        seq = "1"
        if n >= 2:
            for k in range(0,n-1):
                list = [i for i in seq]
                stack = []
                while len(list) > 0:
                    a = list[0]
                    l = 0
                    while len(list) > 0 and a == list[0]:
                        l += 1
                        list.remove(a)
                    stack.append(str(l)+a)
                    
                seq = ''.join(stack)
        return seq
```

## 70. Climbing Stairs

[Link to the problem](https://leetcode.com/problems/climbing-stairs/)

**Analysis:**

1. This is again a recursive process.   
2. In order to climb *n+1* stairs, one has exactly two possibilities for the previous step: either one reach the *n*th stair, or one reach the *(n-1)*th stair. Thus if we denote by `a(k)` the number of different ways to climb *n* stairs, then we have `a(n+1)=a(n)+a(n-1)` (here we need to assume `n-1>0`). This is the inductive formula!
3. Set up the initial terms `a(0)=a(1)=1` and use the above inductive formula, we can easily get it done via a simple `for` loop.

```
class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1,1]
        for k in range(0,n):
            a.append(a[k]+a[k+1])
            
        return a[n]
```

**Remark:** If one realizes that this is actually the Fibonacci sequence, he could choose to use the explict formula as in [Wikipedia: Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number).

## 344. Reverse String

[Link to the problem](https://leetcode.com/problems/reverse-string/)

**Analysis:** Use `head` to store the head of the unchanged part of the list, and use `tail` to store the tail. Then exchange their positions.

```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
       
        L = (len(s)+1)//2
        for k in range(0, L):
            head = s[k]
            tail = s[-k-1]
            s[k] = tail
            s[-k-1] = head

```

## 58. Length of Last Word

[Link to the problem](https://leetcode.com/problems/length-of-last-word/)

**Analysis:** First use the `.strip()` method to remove any empty space in the beginning and in the end of the string. Then count how many non-empty letters in the tail (from right to left) until we reach to the first empty space.

```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        stripped = s.strip()       
        while k <= len(stripped)-1:
            if stripped[-k-1] != " ":
                k += 1
            else:
                return k
        
        return k
```

## 231. Power of Two

[Link to the problem](https://leetcode.com/problems/power-of-two/)

**Analysis:** One can of course do it in a recursive fashion, that is, divide `n` by 2, check the remainder: if it is non-zero, stop and return `False`; otherwise, update `n=n/2` and repeat. If in the end we get `n=1`, return `True`.

However there is an clever one-liner using the bitwise operations such as `&` and `|`:

```
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1) == 0
```

For a good explaination of the Python bitwise operators, see [Here](https://www.tutorialspoint.com/python/bitwise_operators_example.htm). So the idea of the above solution is: if `n<=0`, return `False`. For the second part, `n&(n-1)==0`, any positive integer `n` is represented uniquely as a sequence of bits, that is, `1`s and `0`s. However, `n` is a power of 2 if and only if the bit form of `n` looks like `10...0`, where there is only a leading `1`, and the rest are all 0s.  In that case, the bit form of `n-1` is `01..1`. Therefore the bitwise *and* operator `n&(n-1)` will give a sequence of 0s, since at each corresponding position for the bit forms of `n` and `n-1`, there is always a `0` and a `1`. Meanwhile, if `n` is not a power of 2, then in the bit form of `n`, there are at least two `1`s, say `...1...1...`. A moment thinking will lead to the conclusion that the bit form of `n-1` will have `1` in the first position, as `...1...*...`, therefore the outcome of `n&(n-1)` is never 0!


## 217. Contains Duplicate

[Link to the problem](https://leetcode.com/problems/contains-duplicate/)

**Analysis:** Change the list to set, then compare the lengths of the list and the set.

```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) != len(nums)
``` 

## 204. Count Primes

[Link to the problem](https://leetcode.com/problems/count-primes/)

**Analysis:**  

1. Build a logic list `res` to store whether the integers for 0 to n-1 are prime or not.
2. Initial conditions: 0 and 1 are not primes, so set the first two elements in `list` to be `False`, while set the third element (which corresponds to 2) to be `True`.
3. Using a `for` loop, we update the list `res`: if `i` is a prime, then `2*i`, `3*i`, etc. are all non-prime.
4. We count how many `True` are in `res`. 

```
class Solution:
    def countPrimes(self, n: int) -> int:
            if n <= 2:
                return 0
            res = [True] * n
            res[0] = res[1] = False
            for i in range(2, n):
                if res[i] == True:
                    for j in range(2, (n-1)//i+1):
                        res[i*j] = False
            return sum(res)
```

## 263. Ugly Number
[Link to the problem](https://leetcode.com/problems/ugly-number/)

**Analysis:**

1. If `num` is strictly greater than 1, we keep trying to reduce it, by dividing `num` by `2,3,5`, if divisible.
2. We use the logic variable `ugly` to track whether `num` is divisible by `2,3,5` or not.

```
class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 1:
            ugly = False
            for k in [2,3,5]:
                if num % k == 0:
                    ugly = True
                    num = num/k
            if not ugly:
                return ugly
        return num == 1
```


## 202. Happy Number

[Link to the problem](https://leetcode.com/problems/happy-number/)

**Analysis:** 

1. Use a list called `history` to store the history of numbers we obtain. The variable `tail` is the current last element in `history`.

2. If `tail` is not 1, we continue the process to add numbers to `history`.

3. Each time we add an element to `history`, we check whether this element has appeared before. If so, then we will get an infinite loop, so we stop the loop.

4. Once we break the loop, we check whether `tail` is 1 or not. If 1, then this number is happy; otherwise, it is an unhappy number.

```
class Solution:
    def isHappy(self, n: int) -> bool:
        history = [n]
        tail = n
        while tail != 1:
            l = [int(i)**2 for i in str(tail)]
            tail = sum(l)
            history.append(tail)
            if len(history) > len(set(history)):
                break
        
        return tail == 1
```    

## 268. Missing Number

[Link to the problem](https://leetcode.com/problems/missing-number/)

**Analysis:** Sort the list first, then compare the position `k` with its value `nums[k]`.

```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for k in range(0,len(nums)):
            if nums[k] == k:
                k += 1
            else:
                break
        return k
```

Another direct solution (kinda cheating imo):

```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        return N(N+1)/2 - sum(nums)
```

## 171. Excel Sheet Column Number

[Link to the problem](https://leetcode.com/problems/excel-sheet-column-number/)

**Analysis:** First build a dictionary to indicate which number each letter in the alphabet to stand for. Then `s` in basically a number in the 26 system. We just need to transform it into a number in the decimal system.

```
class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = [chr(i) for i in range(65, 91)]
        nums = [i for i in range(1, 27)]
        dic = dict(zip(alphabet, nums))
        L = len(s)
        s_list = [dic[s[i]] * (26 ** (L-1-i)) for i in range(0,L)]
     
        return sum(s_list)
```

## 169. Majority Element

[Link to the problem](https://leetcode.com/problems/majority-element/)

**Analysis:** 

1. Compute `L = len(nums)//2`, which is the least number of repetitions for the majority element.
2. Sort the list `nums`.
3. For each element `i` in the set formed from elements in `nums`, get its index in the sorted list `ind`, then check if the `ind + L`th element is equal to `i`. If so, we captured the majority element!
```
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        L = len(nums)//2
        nums.sort()
        for i in set(nums):
            ind = nums.index(i)
            if ind + L <= len(nums)-1: 
                if nums[ind + L] == i:
                    return i
```

## 121. Best Time to Buy and Sell Stock

[Link to the problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Analysis:** 

1. We use `MAX_step` to denote the maximal profit if one chooses to sell on the `k`th day. Note that this quantity can be negative.
2. `MAX_step` at `k` can be obtained from the `MAX_step` at `k-1`: it equals the maximal value between `prices[k]-prices[k-1]`  and `MAX_step+prices[k]-prices[k-1])`.
3. In the `for` loop, we inductively update the current max profit if one chooses to sell the stock on the `1<=i<=k` day.


```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX=0
        MAX_step=0
        L=len(prices)
        if L>=2:
            for k in range(1, L):
                MAX_step = max(prices[k]-prices[k-1], MAX_step+prices[k]-prices[k-1]) 
                MAX=max(MAX, MAX_step)
        
        return MAX
```
## 122. Best Time to Buy and Sell Stock II

[Link to the problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

**Analysis:** Now we allow multiply transactions, this will lead to different analysis.

1. We use `P` to denote the total profit, `buy` the last buy date, and `sell` the last sell date.
2. If the next day price is lower or equal to the price of the previous day, the `buy` date will move forward, to generate more profit. `buy` will stop move forward once positive profit is possible, that is, `prices[buy+1] > prices[buy]`.
3. Once `buy` is fixed, we consider `sell`. First set `sell = buy + 1` (recall that we will always have prices[sell] > prices[buy], due to how we work with `buy` in the previous step). `sell` will move forward if the price keeps increasing strictly. Once the price stops to increase strictly, `sell` stops moving forward.
4. Once we obtain `sell` and `buy` for the next transaction, we update the profit by `P=P+prices[sell]-prices[buy]`.

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            P = 0  #profit
            buy = 0  #buy date
            sell = 0  #sell date
            L = len(prices)
            while buy < L-1:
                
                if prices[buy+1] <= prices[buy]:
                    buy += 1
                else:
                    sell = buy + 1
                    while sell < L-1 and prices[sell+1] > prices[sell]:
                        sell += 1
                    P = P + prices[sell]-prices[buy]
                    buy = sell + 1
            
            return P
```
## 198. House Robber

[Link to the problem](https://leetcode.com/problems/house-robber/)
```
class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now
```
## 219. Contains Duplicate II

[Link to the problem](https://leetcode.com/problems/contains-duplicate-ii/)

**Analysis:** 

1. The idea is very similar to Problem 217. We just need to check that whether any chunk of length `k+1` contains duplicates.
2. Instead of use `set()` to convert a chunk of the list into a set, we use a little trick here: first we find the set from the first chunk. Then as we move to the right, we remove the first element `nums[step-1]` from the set, and then add the next element `nums[step+k]`  to the set.

```
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = len(nums)
        if L <= 1 or k == 0:
            return False
        elif L <= k+1:
            return len(set(nums)) != L
        else:
            s = set(nums[0:k+1])
            if len(s) != k+1:
                return True
            for step in range(1, L-k):
                s.remove(nums[step-1])
                s.add(nums[step+k])
                if len(s) != k+1:
                    return True
           
                    
            return False
```

## 172. Factorial Trailing Zeroes

**Analysis:** It is the same as count the exponent of 5 in the prime factorization of n-factorial. We first see how many numbers from 1 to n are divisible by 5 : `n//5`. For the numbers which can be divided by 25, we have to count them twice, the first time is already included in the previous step, so we need to add how many numbers can be divided by 25, which can be obtained by `(n//5)//5`. We continue until the remainder is 0.
 
```
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            k=0
            while n > 0:
                k += n//5
                n = n//5
            return k
```
## 168. Excel Sheet Column Title

[Link to the problem](https://leetcode.com/problems/excel-sheet-column-title/)

```
class Solution:
    def convertToTitle(self, n: int) -> str:
        a = [chr(i) for i in range(65,91)]
        b = [i for i in range(0, 26)]
        order = dict(zip(b,a))
        s = ''
        while n > 0:
            s = order[(n-1)%26] + s
            n = (n-1)//26
        return s
```
## 167. Two Sum II - Input array is sorted

[Link to the problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

```
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = set([])
        for i in range(len(numbers)):
            if target-numbers[i] in s:
                return [numbers.index(target-numbers[i])+1,i+1]
            else:
                s.add(numbers[i])
```

## 3. Longest Substring Without Repeating Characters (M)

**Analysis:** `s_n` is the longest substring without repeating characters which ends at the `n`th position. `L_n = len(s_n)` and `L` is the current maximal length.  

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        s_n = ''
        L_n = 0
        dic = set([])
        if len(s) == 0:
            return L
        else:
            for n in range(len(s)):
                if s[n] in dic:
                    s_n = s_n[s_n.index(s[n])+1: ]+s[n]
                    dic = set(s_n)
                    L_n = len(dic)
                else:
                    s_n = s_n + s[n]
                    dic.add(s[n])
                    L_n += 1
                    if L_n > L:
                        L = L_n
            return L
```
## 4. Median of Two Sorted Arrays (H)

For a detailed explanation of the solution, see https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation.
```
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: 
                    max_of_left = nums2[j-1]
                elif j == 0: 
                    max_of_left = nums1[i-1]
                else: 
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: 
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return float((max_of_left + min_of_right) / 2)

```
## 21. Merge Two Sorted Lists

[Link](https://leetcode.com/problems/merge-two-sorted-lists/)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = ListNode(0)
        current = s
        
        if not l1:
            return l2
        if not l2:
            return l1
        else:
            
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    current = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    current = l2
                    l2 = l2.next
        
        
            if l1:
                current.next = l1
            elif l2: 
                current.next = l2
        
        return s.next
            
```
## 83. Remove Duplicates from Sorted List

[Link](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)


```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        if head:
            next_node = head.next
            while next_node:
                if current.val != next_node.val:
                    current.next = next_node
                    current = next_node
                    next_node = current.next
                else:
                    next_node = next_node.next
            current.next = None
            return head 
        else:
            return head
```
## 876. Middle of the Linked List

[Link](https://leetcode.com/problems/middle-of-the-linked-list/)


```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nxt = head.next
        current = head
        L=1
        while nxt:
            nxt = nxt.next
            L +=1
        for i in range(L//2):
            current = current.next
        return current
```

## String Permutation

**Problem Statement:** Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.  If a character is repeated, treat each occurence as distinct, for example an input of `'xxx'` would return a list with 6 "versions" of `'xxx'`

For example, given `s='abc'` the function should return `['abc', 'acb', 'bac', 'bca', 'cab', 'cba']`

```
def perm(s):
    l = []
    if len(s) <= 1:
        l.append(s)
    else:
        for i in range(len(s)):
            for w in perm(s[1:]):
                l.append(s[0]+w)
            s = s[1:]+s[0]
    return l
```

## 141. Linked List Cycle

[Link](https://leetcode.com/problems/linked-list-cycle/)

The first solution is simply recording all the appeared nodes in a set, and traverse the linked list. Each step we check whether the next node is in the appeared list, if yes, then there is cycle, otherwise no cycle.

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        appeared =set([])
        while head:
            if head not in appeared:
                appeared.add(head)
                head = head.next
            else:
                return True
        return False
```
The second approach is to traverse the linked list in two difference paces, one is `slow` and one is `fast`. If there is a cycle, then before the fast one hit `None`, he will catch up with the slow one. 

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        else:
            slow = head
            fast = head.next
            while fast.next and fast.next.next:
                if slow == fast:
                    return True
                else:
                    slow = slow.next
                    fast = fast.next.next
            return False
```
## 2. Add Two Numbers

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        current_value = l1.val +l2.val
        
        l3 = ListNode(current_value % 10)
        head = l3
        
        while l1.next and l2.next:
            
            l1 = l1.next
            l2 = l2.next
            
            
            if current_value > 9:
                
                next_value = l1.val + l2.val + 1
            else:
                next_value = l1.val + l2.val
            
            current_value = next_value
            l3.next = ListNode(current_value % 10)
            l3 = l3.next
        
        while l1.next:
            l1 = l1.next
            
            if current_value > 9:
                
                next_value = l1.val + 1
            else:
                next_value = l1.val 
            
            current_value = next_value
            l3.next = ListNode(current_value % 10)
            l3 = l3.next
        
        
        while l2.next:
            l2 = l2.next
            
            if current_value > 9:
                
                next_value = l2.val + 1
            else:
                next_value = l2.val 
            
            current_value = next_value
            l3.next = ListNode(current_value % 10)
            l3 = l3.next
        
        if current_value > 9:
            l3.next =ListNode(1)
            
        return head
        
```
## 125. Valid Palindrome

```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        regex = re.compile('[^a-zA-Z0-9]')
        #First parameter is the replacement, second parameter is your input string
        s = regex.sub('', s)
        
        
        
        L= len(s)
        i=0

        if len(s) <= 1:
            return True
        else:
            while i <= len(s)//2 - 1:
                
                if s[i].lower() == s[-(i+1)].lower():
                    i += 1
                else:
                    return False
            return True
```
## 680. Valid Palindrome II

```
class Solution:
    def check(self, s:str) -> bool:
        if len(s) <=1:
            return True
        else:
            i=0
            while i <= len(s)//2-1:
                if s[i] != s[-i-1]:
                    return False
                else:
                    i +=1
            return True
           
            
        
    def validPalindrome(self, s: str) -> bool:
        if len(s)<=2:
            return True
        
        else:
            i=0
            while s[i] == s[-i-1]:
                if i == len(s)//2 -1:
                    return True
                else:
                    i+=1
                
            
            if self.check(s[i+1:len(s)-i]) != True:
                return self.check(s[i:len(s)-i-1])
            return True
```

The same idea implemented slightly differently:
```
class Solution:
   def check(self, ss):
       # two pointers
       # move toward center if same
       
       l = 0
       r = len(ss) - 1
           
       while l < r:
           if ss[l] == ss[r]:
               l += 1
               r -= 1
           else:
               return (False, l, r)
       return (True, 0,0)
   
   def validPalindrome(self, s: str) -> bool:
       
       out, l, r = self.check(s)
       if out:
           return True
       # if not the same, check if s[l+1] == s[r] or s[l] == s[r+1], del flag
       
       else:
           return self.check(s[l+1:r+1])[0] or self.check(s[l: r])[0]
```
## 605. Can Place Flowers

Using recursion:

```
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        elif n > 0 and len(flowerbed)==0:
            return False
        else:
            if flowerbed[0]==1:
                if len(flowerbed) >2:
                    return self.canPlaceFlowers(flowerbed[2:], n)
                else:
                    return False
            if flowerbed[0] == 0:
                if len(flowerbed) ==1:
                    n -= 1
                    flowerbed[0] =1
                    return self.canPlaceFlowers(flowerbed, n)
                if len(flowerbed) >1:
                    if flowerbed[1] ==0:
                        flowerbed[0] = 1
                        n -= 1
                        return self.canPlaceFlowers(flowerbed, n)
                    else:
                        if len(flowerbed) > 3:
                            return self.canPlaceFlowers(flowerbed[3:],n)
                        else:
                            return False
            
```

Using iteration:

```
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        L= len(flowerbed)
        while i < L:
            if n == 0:
                return True
            
            if flowerbed[i] == 1:
                i+=2
            elif flowerbed[i] == 0 and i+1<L:
                if flowerbed[i+1] == 1:
                    i+=3
                else:
                    n-=1
                    i+=2
            else:
                i+=2
                n-=1
        return n<=0
```

## 292. Nim Game

We can actually get the general formula for the outcome: if n is divisible by 4, then the first player loses; otherwise he will win. 
```
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 ==0:
            return False
        else:
            return True
```
## 283. Move Zeroes

```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        num_zeros=0
        j=0
        while i<len(nums):
            if nums[i]==0:
                i+=1
                num_zeros+=1
            else:
                if num_zeros == 0:  ## if no zeros appeared before, simply move forward
                    i+=1
                    j+=1
                else:            ## otherwise,interchange 0 and the non-0 number then forward
                    nums[j]=nums[i]
                    nums[i]=0
                    j+=1
                    i+=1
```
## 278. First Bad Version

Typical binary search
```
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(n) == False:
            return "No bad!"
        else:
            head =1
            tail =n
            mid=(head+tail)//2
            while mid>head:
                if isBadVersion(mid):
                    tail= mid
                    mid=(head+tail)//2
                else:
                    head = mid
                    mid=(head+tail)//2
                    
            if isBadVersion(mid):
                return head
            else:
                return tail
```
## 374. Guess Number Higher or Lower

Simply binary search.

```
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        tail = n
        mid =(head+tail)//2
        while mid>head:
            if guess(mid)==-1:
                tail=mid
                mid=(head+tail)//2
            elif  guess(mid)==1:
                head=mid
                mid=(head+tail)//2
            else:
                return mid
        if guess(head)==0:
            return head
        else:
            return tail
```
## 371. Sum of Two Integers

A nice exercise on bit manipulations. 
```
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == -b:
            return 0
        if abs(a) > abs(b):
            a, b = b, a
        if a < 0:
            return -self.getSum(-a, -b)
        while b:
            c = a & b
            a ^= b
            b = c << 1
        return a
                
```

## 342. Power of Four

If `num` is non-positive, False.
Check if it is a power of 2: if `num & (num-1)` is 0 then we are good.
Check if it is a power of 4: if `num%3==1`, we are good.

```
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
      
        else:
            
            return  not(num & (num-1)) and num%3==1
```

## 155. Min Stack

In order to retrieve the minimal value in constant time, we sacrifice space to store the minimal values at each step of the stack.

```
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        self.min = float('inf')
        self.min_record = []
        

    def push(self, x: int) -> None:
        self.val.append(x)
        if self.min > x:
            self.min = x
            self.min_record.append(x)
        elif self.min == x:
            self.min_record.append(x)
        else:
            self.min_record.append(self.min)

    def pop(self) -> None:
        if len(self.val)>0:
            
            self.val.pop()
            self.min_record.pop()
            if len(self.val)>0:
                self.min = self.min_record[-1]
            else:
                self.min = float('inf')
        else:
            print ('There is nothing to pop!')

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

```
## 345. Reverse Vowels of a String

```
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u'])
        L = len(s)
        H = 0
        T = L-1
        temp = list(s)
        while H < T:
            while temp[H].lower() not in vowels and H < T:
                H += 1
            while temp[T].lower() not in vowels and T > H:
                T -= 1
            
            if H < L and T >= 0:
                temp[H], temp[T] = temp[T], temp[H]
                
                H += 1
                T -= 1
            
            
        
        return ''.join(temp)
```
## 443. String Compression
 
Leetcode is not working for my code. It works well on Spyder with Python 3.7 on my laptop.

```
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        L=len(chars) 
        current=1           ## track the location of the modified list
        step=1              ## step is to keep track of where we are at in the original list
        count=1             ## track the count of continuous appearance of the letter
        
        ## if length is no larger than 1, no need to modify
        
        if L<=1:
            return L
            
        else:
            letter=chars[0]
            while step < L:
                ## if the next letter is the same as the current letter, count+1, step+1 and pop it out
                
                if letter == chars[current]:
                    count += 1
                    step += 1
                    chars.pop(current)
                
                ## if the next letter is different with the current letter, we update the list
                
                else:
                    ## if count is 1, we do not need to add a number, so just move on to the next letter
                    
                    if count == 1:
                        
                        letter = chars[current]
                        current += 1
                        step += 1
                    ## if count>1, we need to add a number after the current letter, then move on the next letter
                    
                    else:
                        letter = chars[current]
                        temp = list(str(count))
                        chars = chars[:current]+temp+chars[current:]
                        current += len(temp)+1
                        step += 1
                        count = 1
                        
            ## edge case: after getting to the end of the list, we need to attach the count number if needed
            
            if count > 1:
                temp = list(str(count))
                chars = chars+temp
                print(chars)
            
            return len(chars)
                        
```
## 367. Valid Perfect Square

```
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L=len(str(num))//2
        temp=0
        while L>=0:
            i=9
            
            while (temp+i*(10**L))**2 > num:
                i-=1
            
            temp=temp+i*(10**L)
            L-=1
            
        return (temp**2) == num
        
```
## 414. Third Maximum Number
```
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1=nums[0]
        max2=float('-inf')
        max3=float('-inf')
        i=0
        for i in range(len(nums)):
            if nums[i] > max1:
                max3, max2 = max2, max1
                max1 = nums[i]
                i+=1
            elif nums[i] == max1 or nums[i]==max2 or nums[i]==max3:
                i+=1
            elif nums[i] < max1 and nums[i] > max2:
                max2, max3 = nums[i], max2
                i+=1
            elif nums[i]< max2 and nums[i] > max3:
                max3=nums[i]
                i+=1
                
            else:
                i+=1
        if len(set([max1,max2,max3]))==3 and max3>float('-inf'):
            return max3
        else:
            return max1
```
## 504. Base 7

```

class Solution:
    def convertToBase7(self, num: int) -> str:
        i=8
        sign = 1
        s=0
        if num==0:
            return '0'
        if num<0:
            sign = -1
            num = -num
            print(num)
        while i >= 0:
            power = 7**i
            j=1
            while j*power<=num:
                j+=1
            
            j-=1
            num = num-j*power
            s+=j*(10**i)
            i-=1
        
        return str(sign*s)
        
```
## 383. Ransom Note
```
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        
        dict1=dict(zip([chr(i) for i in range(ord('a'),ord('z')+1)], [0]*26))
        
        L1=len(ransomNote)
        L2=len(magazine)
        if L1==0:
            return True
        else:
            if L2==0:
                return False
            else:
                i=1
                while i<=L1:
                    dict1[ransomNote[i-1]] += 1
                    i+=1
                
                j=1
                while j<=L2:
                    dict1[magazine[j-1]] -=1
                    j+=1
                
            if max(dict1.values()) > 0:
                return False
            else:
                return True
```
## 541. Reverse String II
```
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        L=len(s)//(2*k)
        remainder=len(s)%(2*k)
        while i < L:
            
            
            s = s[:2*k*i]+s[2*k*i:2*k*i+k][::-1]+s[2*k*i+k:]
            i+=1
            
        if remainder > k:
            s = s[:2*k*i]+s[2*k*i:2*k*i+k][::-1]+s[2*k*i+k:]
        elif remainder > 0:
           
            
            s = s[:2*k*i]+s[2*k*i:2*k*i+k][::-1]
        
            
        
        return s
            
```
## 557. Reverse Words in a String III
```
class Solution:
    def reverseWords(self, s: str) -> str:
        start=0
        end=0
        L=len(s)
        if L==0:
            return s
        else:
            while end < L:
                if s[end]!=' ':
                    end+=1
                else:
                    s=s[:start]+s[start:end][::-1]+s[end:]
                    start = end+1
                    end+=1
                    
            if start < L:
                s = s[:start]+s[start:][::-1]
```

## 682. Baseball Game

```
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        clean =[]
        L=len(ops)
        i=0
        while i < L:
            if ops[i]=='C':
                clean.pop()
                i+=1
            elif ops[i]=="+":
                clean.append(clean[-2]+clean[-1])
                i+=1
            elif ops[i]=='D':
                clean.append(clean[-1]*2)
                i+=1
            else:
                clean.append(int(ops[i]))
                i+=1
        return sum(clean)
```
## 633. Sum of Square Numbers
```
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j=0
        
        while j**2 <= c/2:
            if math.sqrt(c-j**2).is_integer():
                return True
            else:
                j+=1
        return False
        
```
## 520. Detect Capital

```
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        s=set([chr(i) for i in range(ord('A'),ord('Z')+1)])
        i=0
        cap_num=0
        if word[0] in s:
            for i in range(0,len(word)):
                if word[i] in s:
                    cap_num+=1
                    i+=1
                    
                else:
                    i+=1
            if cap_num==len(word) or cap_num==1:
                return True
            else:
                return False
            
        else:
            for i in range(0,len(word)):
                if word[i]  in s:
                    return False
                else:
                    i+=1
            return True
```
## 686. Repeated String Match

```
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        if len(set(B)-set(A))>=1:
            return -1
        else:
            
            LB=len(B)
            A_temp =A
            count=1
            while len(A_temp)<LB:
                A_temp = A_temp+A
                count+=1
            if B in A_temp:
                return count
            else:
                A_temp += A
                count+=1
                if B in A_temp:
                    return count
                else:
                    return -1
```
## 412. Fizz Buzz

```
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[str(i+1) for i in range(n)]
        i1=3
        i2=5
        i3=15
        while i1 < n+1:
            l[i1-1]="Fizz"
            i1 += 3
        while i2 < n+1:
            l[i2-1]='Buzz'
            i2 += 5
        while i3 < n+1:
            l[i3-1]='FizzBuzz'
            i3 += 15
        return l
```
## 977. Squares of a Sorted Array

__Main idea:__ Use two pointers to get the next largest square.
```
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        answer = [0] * len(A)
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer
```
## 970. Powerful Integers

First approach is brute-force. Be aware of the edge case that either x or y is 1 and the edge case that bound is less than 2.

```
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        s=set()
        i,j=0,0
        sum=2
        x,y=max(x,y),min(x,y)
        
        if x==1:
            if bound >=2:
                return [2]
            else:
                return []
        elif y==1:
            while sum<=bound:
                s.add(sum)
                i+=1
                sum=x**i + 1
        else:
            
            while sum<=bound:
                s.add(sum)
                j+=1
                sum=1+y**j


            while j>=0:
                i=1
                sum=x**i+y**j
                while sum<=bound:
                    s.add(sum)
                    sum=x**i+y**j
                    i+=1
                j-=1

        return list(s)
```

Second approach is to record the powers of x up to bound, and the powers of y up to bound. Then add the two lists while keeping the sums which is less than or equal to the bound.

```
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []
        
        
        xpower,ypower,i,j=[],[],0,0
        if x==1:
            xpower=[1]
        else:
            while x**i<=bound:
                xpower.append(x**i)
                i+=1
        
        if y==1:
            ypower=[1]
        else:
            while y**j<=bound:
                ypower.append(y**j)
                j+=1
                
        return list(set([x+y for x in xpower for y in ypower if x+y<=bound]))
        
```
## 290. Word Pattern

Idea: use a dictionary to keep track of the pattern. Be aware of that the unique letters in `pattern` and the unique words in the string should be the same.

```
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s=str.split()
        if len(pattern)!=len(s) or len(set(pattern))!=len(set(s)):
            return False
        else:
            tracking = {}
            i=0
            while i<len(pattern):
                if pattern[i] not in tracking.keys():
                    tracking[pattern[i]]=s[i]
                    i+=1
                else:
                    if tracking[pattern[i]] != s[i]:
                        return False
                    else:
                        i+=1
            return True
```
## 645. Set Mismatch
```
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        missing = list(set([i+1 for i in range(n)])-set(nums))[0]
        duplicate =  int(-n*(n+1)/2 +sum(nums)+missing)
        return [ duplicate,missing]
```

## 287. Find the Duplicate Number

This problem can be solved using the [Floyd's Tortoise and Hare](https://en.wikipedia.org/wiki/Cycle_detection) or Floyd's cycle detection algorithm. Essentially we are treating the list with duplicates as a linked list with cycles.

```
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[nums[0]]
        
        ## identifying whether there is cycle or not
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        ## now find the entry of the cycle, where our duplicate resides. 
        
        fast=0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow
```

## 387. First Unique Character in a String

Approach 1: using a dictionary to track the number of appearance.

```
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = [i,1]
                i+=1
            else:
                dic[s[i]][1] += 1
                i+=1
        for key in dic.keys():
            if dic[key][1]==1:
                return dic[key][0]
        return -1
```

Approach 2: This is due to [gregs.](https://leetcode.com/problems/first-unique-character-in-a-string/discuss/86351/Python-3-lines-beats-100-(~-60ms)-!)
As one of the comments explained: 'Its only faster because s.index is a C function that python is calling. So you are changing the python loop to be the 26 characters, and the C loop is doing the heavy lifting searching the string. From an algo perspective this is slower than the others.'
```

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
```

## 507. Perfect Number

```
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        else:
            i=2
            sum=1
            SQRT=num**(0.5)


            while i < SQRT:
                if num%i==0:
                    sum = sum+i+num//i
                i+=1
            if int(SQRT)==SQRT:
                sum += SQRT
            
            print(sum)

            return sum == num
```
## 447. Number of Boomerangs

__Idea__: for each point in the list, we use a dictionary `cmap` to record the distances between it and other points in the list and how many points shares this distance.

```
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res
        
```
## 485. Max Consecutive Ones
```
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = "".join([str(i) for i in nums]).split('0')
        return max([len(j) for j in temp])
```
## 349. Intersection of Two Arrays

```
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
```

## 350. Intersection of Two Arrays II

```
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1=Counter(nums1)
        c2=Counter(nums2)
        temp=[]
        for i in c1:
            if i in c2:
                temp+= [i]*min(c1[i],c2[i])
        return temp
```
## 496. Next Greater Element I
```
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L2=len(nums2)
        if L2==0:
            return []
        
        output=[]
        M=max(nums2)
        
        for i in range(len(nums1)):
            
            if nums1[i] >= M:
                output.append(-1)
                i += 1
            else:
                
                t=nums1[i]
                j=nums2.index(t)
                while j<L2 and nums2[j] <= t:
                    j += 1
                if j<L2:
                    output.append(nums2[j])
                else:
                    output.append(-1)
                i += 1
        return output
```

## 509. Fibonacci Number


__Mesmorization approach:__

```
class Solution:
    def fib(self, N: int) -> int:
        cache={0:0,1:1}
        for i in range(2,31):
            cache[i]=cache[i-1]+cache[i-2]
            i += 1
        return cache[N]
        
```
__Iterative approach:__

```
class Solution:
    def fib(self, N: int) -> int:
       
        a,b = 0,1
        for _ in range(N):
            a, b = b, a+b
        return a 
```
## 409. Longest Palindrome

__Idea:__ First list the number of appearances for each letter in the string by using the `Counter` function. Then notice that if the count is even, then we can make use all of the repetitions of that letter to form a Palindrome; if the count is odd, then we can make use of all except one repetition of that letter. Finally, if odd counts ever happened, note that we can choose of the letters with odd counts in the center of the palindrome, so we need to add 1 to the total maximal length.

```
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)
        length=0
        max_odd=0
        for i in counter:
            if counter[i]%2==0:
                length += counter[i]
            else:
                length += counter[i]-1
                max_odd = 1
        if max_odd == 1:
            return length + 1
        else:
            return length
        
```

## 463. Island Perimeter

```
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        elif len(grid)==1:
            return 2*(sum(grid[0]))+2
        
        
        hight = len(grid)
        width = len(grid[0])
        
        # horizontal sum:
        
        h_first, h_last = sum(grid[0]), sum(grid[-1])
        h_sum = h_first + h_last
        for i in range(0,hight-1):
            for j in range(width):
                if (grid[i][j]==1 and grid[i+1][j]==0) or (grid[i][j]==0 and grid[i+1][j]==1):
                    h_sum += 1
                    j += 1
            i += 1
        
        # vertical sum:
        
        v_sum=0
        for i in range(hight):
            s='0' + "".join([str(e) for e in grid[i]]) + '0'
            v_sum = v_sum + s.count('01')+s.count('10')
            i += 1
        
        return v_sum+h_sum
```
## 434. Number of Segments in a String
```
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
```
## 693. Bitwise Alternating Numbers

```
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        k= ((n<<1) ^ n) >>1
        return (k+1)&k==0
```
## 438. Find All Anagrams in a String
```
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        
        
        output=[]
        from collections import Counter
        p_count = Counter(p)
        for i in range(ord('a'),ord('z')+1):
            if chr(i) not in p_count:
                p_count[chr(i)]=0
                i += 1
        L=len(p)
        s_count=Counter(s[:L])
        for i in range(ord('a'),ord('z')+1):
            if chr(i) not in s_count:
                s_count[chr(i)]=0
                i += 1
                
        for i in range(len(s)-L):
            
            if s_count==p_count:
                output.append(i)
            
            s_count[s[i]] -= 1
            s_count[s[i+L]] +=1
            i+=1
        if s_count==p_count:
            output.append(i)
        return output
```
## 242. Valid Anagram

```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        from collections import Counter
        return Counter(s)==Counter(t)
            
```
## 1071. Greatest Common Divisor of Strings

```
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if set(str1)!=set(str2):
            return ''
        
        elif len(str1)==0 or len(str2)==0:
            return ''
        
        if len(str1)>len(str2):
            str1, str2 = str2, str1
        
        from math import gcd
        gcd=gcd(len(str1),len(str2))
        
        divisor=str1[:gcd]
        
        if divisor*(len(str1)//gcd)==str1 and divisor*(len(str2)//gcd)==str2:
            return divisor
        else:
            return ''
```
## 1047. Remove All Adjacent Duplicates In String
```
class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)
```

## 566. Reshape the Matrix

```
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)==0 or nums[0]==0:
            return nums
        
        if len(nums)*len(nums[0])!=r*c:
            return nums
        
        l=len(nums[0])
        
        output = [[0]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                output[i][j]=nums[(i*c+j)//l][(i*c+j)%l]
                j+=1
            i+=1
        return output
            
```
## 728. Self Dividing Numbers

```
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        output=[]
        num=left
        while num<=right:
            if self.check_self_dividing(num):
                output.append(num)
            num += 1
        return output
    
    def check_self_dividing(self, n):
        last, temp = n%10, n//10
        while temp>0:
            if last==0 or n%last!=0:
                return False
            else:
                last, temp = temp%10, temp//10
        return n%last==0
```
## 575. Distribute Candies

```
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)), len(candies)//2)
```
## 191. Number of 1 Bits

```
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp=n
        total=0
        while temp>0:
            temp, total = temp//2, total+temp%2
        return total
```


## 100. Same Tree

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif (p and not q) or ((not p) and q):
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
```
## 101. Symmetric Tree

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False
```
## 104. Maximum Depth of Binary Tree

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root and not root.left and not root.right:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

## 111. Minimum Depth of Binary Tree

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and  not root.right:
            return 1
        elif not root.left and root.right:
            return 1+self.minDepth(root.right)
        elif not root.right and root.left:
            return 1+self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

## 112. Path Sum

__Main idea:__ we traverse the tree using a stack. In order to keep the path sum information, we keep the current sum from the root to the current position next to each node in the tree. Each time we pop an item from the stack, we check if the corresponding node has branches or not. If no branch, then it is a leaf, we record the path sum to the `sum_list`.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return sum in self.listPathSum(root)
    
    def listPathSum(self, root):
        if not root:
            return []
        else:
            
            sum_list=[]
            stack=[[root, root.val]]
            
            while stack!=[]:
                temp=stack.pop()
                cur_node=temp[0]
                cur_sum=temp[1]
                if not cur_node.left and not cur_node.right:
                    sum_list.append(cur_sum)
                    
                    
                else:
                    if cur_node.left:
                        stack.append([cur_node.left, cur_node.left.val+cur_sum])
                    if cur_node.right:
                        stack.append([cur_node.right, cur_node.right.val+cur_sum])
            return sum_list
                
                
```
## 107. Binary Tree Level Order Traversal II

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        stack = [root]
        res, data = [],[]
        nCount = 1 # keep track of number of nodes on the current level
        while stack != []:
            temp = stack.pop(0) # the popping order is 'first come, first pop'
            nCount -= 1
            data += [temp.val]
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            if nCount == 0: # once we clear an entire level, append data to the head of res, reset data and nCount
                res = [data] + res
                data = []
                nCount =  len(stack)
        
        return res
```

## 237. Delete Node in a Linked List

__Idea:__ Swapping the values of the nodes. In the end, update the tail.

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        while node.next:
            node.val=node.next.val
            cur=node
            node=node.next
        cur.next=None
```
## 203. Remove Linked List Elements

__Idea:__ The main edge cases are that the head node has the value same as `val` and the last node has the value same as `val`.
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        new_head = head
        while new_head.val == val and new_head.next:
            new_head = new_head.next
        if new_head.val == val:
            new_head = None
            return new_head
        
        
        
        cur = new_head        
        while cur.next:
            if cur.val == val:
                cur.val = cur.next.val
                cur.next = cur.next.next
            else:
                prev = cur
                cur = cur.next
        if cur.val == val:
            prev.next = None
        
        return new_head
```
## 206. Reverse Linked List

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        
        
        if head.next:
            cur = head.next
            prev = head
            prev.next = None
        
        while cur.next:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        
        cur.next = prev
        
        return cur
        
```
## 234. Palindrome Linked List

__Method 1:__ (Time O(n), space O(n)) Brutal force-record the linked list elements in order with a list, then check whether the list is polidrome or not.

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l=[]
        cur=head
        while cur:
            l.append(cur.val)
            cur = cur.next
        return l==l[::-1]
```

__Method 2:__  (Time O(n), space O(1)) Use a fast pointer and a slow pointer.   `fast` moves 2 steps at a time while `slow` moves 1 step at a time. Meanwhile, `rev` is used to reverse the first half. Then check whether the reversed first half is equal to the second half.

```
def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev
```
## 160. Intersection of Two Linked Lists

__Method 1:__ (Time O(n), Space O(1)) First determine which linked list is longer, then start with the positions at which to both ends are equal, and move at same pace.

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        
        if lenA > lenB:
            headA, headB, lenA, lenB = headB, headA, lenB, lenA
            
        curA,curB = headA,headB
        for i in range(lenB-lenA):
            curB=curB.next
            
        while curB and curB != curA:
            curB = curB.next
            curA = curA.next
        return curA
```

__Method 2:__ First concatenate the two lists. If there is an intersection, there must be a loop in the concatenated list. Then Floyd's cycle detection algorithm will tell us where the start of the loop is located.

```
class Solution(object):
    def getIntersectionNode(self, A, B):
        if not A or not B: return None

        # Concatenate A and B
        last = A
        while last.next: last = last.next
        last.next = B

        # Find the start of the loop
        fast = slow = A
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = A
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow

        # No loop found
        last.next = None
        return None
```
## 303. Range Sum Query - Immutable

```
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accu =[0]
        for n in nums:
            self.accu += [self.accu[-1] + n]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j+1]-self.accu[i]
```

## 500. Keyboard Row

```
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if words == []:
            return []
        
        res = []
        for word in words:
            if self.canTypeOneRow(word):
                res.append(word)
        return res
        
    def canTypeOneRow(self, s):
        r1='QWERTYUIOPqwertyuiop'
        r2='ASDFGHJKLasdfghjkl'
        r3='ZXCVBNMzxcvbnm'
        
        if s == '':
            return True
        
        if s[0] in r1:
            test = r1
        elif s[0] in r2:
            test = r2
        else:
            test = r3
        for j in range(len(s)):
            if s[j] not in test:
                return False
            else:
                j += 1
        return True
```
## 521. Longest Uncommon Subsequence I


```
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a)>len(b):
            return len(a)
        elif len(b)>len(a):
            return len(b)
        
        if a!=b:
            return len(a)
        else:
            return -1
```
## 120. Triangle

__Idea:__ Starting from the top of the triangle, proceed level by level. For each level, `path_sums` will record the minimal path sums ending at each position on that level. Once we arrive at the bottom, return the minimal path sum.

```
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        path_sums = triangle[0]
        for i in range(1, len(triangle)):
            
            cur_row = triangle[i]
            path_sums = [0] + path_sums
            
            temp = [0]*(i+1)
            temp[0]=path_sums[1]+cur_row[0]
            
            for j in range(1, i):
                temp[j] = min(path_sums[j] + cur_row[j], path_sums[j+1]+cur_row[j])
            
            
            temp[i]=path_sums[i]+cur_row[i]
            path_sums = temp
            
        return min(path_sums)
```
## 665. Non-decreasing Array

__Idea:__ (Time O(n), Space O(1)) This problem turns out to be quite tricky (maybe I was doing it in the wrong perspective). First we check whether there is any inversion in the list, and record the position that it happens: `high, low`. (If no inversion at all, then 'high==len(nums)-1', which we would return True). Next we check that whether the sublist starting at the `low`th position, contains any inversions. If there is one more inversion, then return False. Otherwise, there is just one inversion, then we check whether one can fix the inversion by modifying just one list element : either the `nums[high]` or `nums[low]`. If we can modify `nums[low]` to make it work, then one must have either 'low==len(nums)-1' or 'nums[low+1]>=nums[high]'; or we can modify `nums[high]' to work, then one must have that either  'high==0' or 'nums[high-1]<=nums[low]'.
```
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        i=0
        while i <= len(nums)-2:
            if nums[i] <=  nums[i+1]:
                i += 1
            else:
                
                break
        high, low = i, i+1
        
        
                
        for _ in range(low, len(nums)-1):
            if nums[_] > nums[_ + 1]:
                return False
            else:
                _ += 1
        
        if high == 0 or high==len(nums)-1:
            return True
        elif low == len(nums)-1:
            return True
        else:
            return nums[low+1] >= nums[high] or nums[high-1] <= nums[low]
```

## 108. Convert Sorted Array to Binary Search Tree

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        L = len(nums)
        if L==0:
            head = None
        else:
            head = TreeNode(nums[L//2])
            head.left = self.sortedArrayToBST(nums[:L//2])
            head.right = self.sortedArrayToBST(nums[L//2+1:])
            
        return head
```
## 110. Balanced Binary Tree

__Method 1:__ (Time O(nlogn)) Brutal force: compute the depth of the left subtree and right subtree, respectively, then recursively go over all the tree and check whether every node is balanced.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif self.TreeDepth(root.left) >= self.TreeDepth(root.right) + 2:
            return False
        elif self.TreeDepth(root.right) >= self.TreeDepth(root.left) + 2:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def TreeDepth(self, root):
        if not root:
            return 0
        
        depth = 0
        stack = [root]
        count = 1
        while stack != []:
            temp = stack.pop(0)
            count -= 1
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            
            if count == 0:
                depth += 1
                count = len(stack)
        return depth
```
__Method 2__ (Time O(n)): Instead of computing the depth for each subtree and then compare, which leads to a whole lot of repetitions, we simply run the depth function once for the head node, which actually can compute the depth for each subtree. We check the condition in the depth function. (Here we use the recursive definition of the depth function.)
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = False
        self.getHeight(root)
        return not self.flag
        
    
    def getHeight(self, root):
        if not root: return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1: 
            self.flag = True
        return max(left, right) + 1
```
## 15. 3Sum

__Idea:__ These '3Sum' problems are a bit challenging. The idea is that one first sort the array, then use three pointers to traverse the entire array. Depending on what exactly the goal is, we may need to implement the code slightly differently.

```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            res = []
            nums.sort()
            for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                l, r = i+1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s < 0:
                        l +=1 
                    elif s > 0:
                        r -= 1
                    else:
                        res.append((nums[i], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1
            return res
```
## 16. 3Sum Closest

```
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        s, dif = float('inf'), float('inf')
        for i in range(len(nums)-2):
            h, t = i+1, len(nums)-1
            while h < t:
                temp_sum = nums[i] + nums[h] + nums[t]
                temp_dif = abs(target-temp_sum)
                if temp_dif < dif:
                    s, dif = temp_sum, temp_dif
                
                if temp_sum == target:
                    return target
                elif temp_sum > target:
                    t -= 1
                else:
                    h += 1
            
        return s
```
## 923. 3Sum With Multiplicity


__Method 1:__ Same idea as the previous _sort and traverse_ strategy. Not very efficient, O(N^2) time complexity. Sutle point at whether the 2nd and 3rd pointer have the same value or not.
```
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        res = 0
        A.sort()
        for i in range(len(A)-2):
            
            head, tail = i+1, len(A)-1
            
            while head < tail:
                s = A[i]+A[head]+A[tail]
                if s < target:
                    head += 1
                elif s > target:
                    tail -= 1
                else:
                    if A[head] == A[tail]:
                        temp = (tail-head+1)*(tail-head)//2
                        res += temp
                        break
                    else:
                        
                        left, right = 1, 1
                        while head < tail-1 and A[tail-1]==A[tail]:
                            right += 1
                            tail -= 1
                        while head < tail-1 and A[head+1]==A[head]:
                            left += 1
                            head += 1
                        temp = left*right
                        res, head, tail = res + temp, head + 1, tail - 1
            i += 1
        return res%(10**9+7)
```
__Method 2:__ Make use the `Counter` function from `collections`. Greatly reduce the time required to repetedly traverse the array for counting as in the previous method.

```
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        
        c = collections.Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k: res += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j: res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)
```

## 189. Rotate Array

__Method 1:__ (Time O(n^2), Space O(1)) This is the brutal force method. We first define the function `rotate1`, which rotates the given array to the right by 1 position. Then in the main function `rotate`, we apply this `k%len(nums)` times.
```
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=1
        k=k%len(nums)
        while i <= k:
            self.rotate1(nums)
            i += 1
    
    def rotate1(self, s):
        temp = s[-1]
        i = len(s)-1
        while i >= 1:
            s[i] = s[i-1]
            i -= 1
        s[0] = temp
```


__Method 2:__  (Time O(n), Space O(k)) First store the last k elements in order, then rotate the first `len(nums)-k` elements to their correct positions, finally update the first k positions.

```
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        L= len(nums)
        k = k % L
        temp = nums[L-k:]
        for j  in range(L-k):
            nums[L-j-1]=nums[L-j-k-1]
            j += 1
        
        for i in range(k):
            nums[i]=temp[i]
            i += 1
```

__Method 3:__ (Time O(n), Space O(1)) Very nice solution. Swapping the last k elements to the correct position, then do the same swapping process for the rest (n-k) elements. Keeping doing this until done. Note that we need to update the length of array.
```
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in range(k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i]
            n, j = n - k, j + k
            k = k % n
```

## 235. Lowest Common Ancestor of a Binary Search Tree

__Idea:__ First check whether the one of the given nodes is an ancestor of the other, if yes, return that node. If the two nodes do not have an ancestial relation, then we search from the root. There are two possibilities:
the two nodes are on the same branch of the root, or the two nodes are on different branches (this is because we have a BST). For the first case, we move down to that branch; for the second case, the root must be the lowest common ancestor. In addition, to avoid repetedly checking whether `p,q` share ancestial relation or not, we introduce a new function `lowestAncestorSimple`, which finds the lowest common ancestor recursively, given that the two nodes do have have ancestial relation with each other.  

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if self.isAncestor(p, q):
            return p
        if self.isAncestor(q, p):
            return q
        else:
            return self.lowestAncestorSimple(root, p, q)
            
    def lowestAncestorSimple(self, root, p, q):
    
        ## Find the lowest common ancestor given that p, q do not have ancestial relations.
        
        if (p.val > root.val and q.val < root.val) or (p.val<root.val and q.val>root.val):
            return root
        elif p.val > root.val and q.val > root.val:
            return self.lowestAncestorSimple(root.right, p, q)
        else:
            return self.lowestAncestorSimple(root.left, p, q)
                    
    
    def isAncestor(self, node1, node2):
        ## checking whether node1 is an ancestor of node2
        
        stack = [node1]
        while stack != []:
            temp = stack.pop(0)
            if temp.left == node2 or temp.right == node2:
                return True
            else:
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
        return False
        
```
## 236. Lowest Common Ancestor of a Binary Tree

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        
        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way, 
        # because in such scenarios, node where 'p' found is LCA
            return left or right
````
## 598. Range Addition II

```
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        L=len(ops)
        if L==0:
            return m*n
        
        m1, m2 = float('inf'), float('inf')
        for i in range(L):
            m1, m2 = min(m1, ops[i][0]), min(m2, ops[i][1])
            i += 1
        return m1*m2
```
## 908. Smallest Range I

```
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        m, M = min(A), max(A)
        return max(M-m-2*K, 0)
```
## 1041. Robot Bounded In Circle
```
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        init, pos = [[0,0],0], [[0,0],0]
        for s in instructions*4:
            self.action(pos, s)
        return init == pos
        
    def action(self, pos, s):
        ## We use a list of two elements to denote the positioning of the robot:
        # 1st element is a list of two integers, which are the coordinates of the position
        # 2nd element is the direction the robot is facing, we use 0-3 (integers mod 4), where 0 
        # stands for North and adding 1 means turning right by 90 degrees
        
        if s == 'L':
            pos[1] = (pos[1]-1) % 4
        elif s == 'R':
            pos[1] = (pos[1]+1) % 4
        else:
            if pos[1]  == 0:
                pos[0][1] += 1
            elif pos[1] == 2:
                pos[0][1] -= 1
            elif pos[1] == 1:
                pos[0][0] += 1
      
            else:
                pos[0][0] -= 1
```
## 709. To Lower Case

```
class Solution:
    def toLowerCase(self, str: str) -> str:
        temp = []
        for i in range(len(str)):
            if 65 <= ord(str[i]) and ord(str[i]) <= 90:
                temp.append(chr(ord(str[i])+32))
            else:
                temp.append(str[i])
        
        return ''.join(temp)
```
## 704. Binary Search

__Method 1:__ recursive approach, time O(log n)
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or nums[-1] < target or nums[0] > target:
            return -1
        
        
        
        if nums[len(nums)//2] == target:
            return len(nums)//2
        else:
            if nums[len(nums)//2] > target:
                return self.search(nums[:len(nums)//2], target)
            else:
                
                if self.search(nums[len(nums)//2:],target) != -1:
                    return len(nums)//2 + self.search(nums[len(nums)//2:],target)
                else:
                    return -1
```
Method 2: using two pointers `left` and   `right`, to indicate the left and right bounds of `nums` to check.
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: 
            return -1
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
         
```

## 455. Assign Cookies

```
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
         
        
        
        left = 0
        
        if len(s) == 0:
            return 0
        
        while left <= len(s)-1 and g!=[] and s[-1]>=g[0]:
            cur = g.pop(0)
            res += 1
            
            while s[left] < cur:
                left += 1
            left +=1
        return res 
```
## 404. Sum of Left Leaves

We use a stack to traverse the binary tree. Each element in the stack records the node and whether the node is left or right. Then we only summing up the values of the left leaves.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        if not root:
            return 0
        
        stack = [[root, 0]]
        while stack != []:
            temp = stack.pop(0)
            node, left = temp[0], temp[1]
            if not node.left and not node.right and left:
                sum += node.val
            
            if node.left:
                stack.append([node.left, 1])
            if node.right:
                stack.append([node.right, 0])
        return sum
```
## 938. Range Sum of BST

Remember to use the structure of a binary search tree!

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        SUM = 0
        stack = [root]
        while stack != []:
            node = stack.pop(0)
            val = node.val
            if L <= val and R >= val:
                SUM += val
            if node.left and val >= L:
                stack.append(node.left)
            if node.right and val <= R:
                stack.append(node.right)
        return SUM
```
##  674. Longest Continuous Increasing Subsequence

__Idea:__ (Time O(n), Space O(1)) tranverse the list once while recording the current maximal length of of continuous increasing subsequence and the current streak. If the next element is not bigger than the previous one, we update the current max length to be the maximum among `max_length` and `cur_streak`. Then we reset the current streak to 1.

```
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        
        max_length = 1
        cur_streak = 1
        i = 1
        while i <= len(nums)-1:
            if nums[i-1] < nums[i]:
                cur_streak += 1
                
            else:
                max_length, cur_streak = max(max_length, cur_streak), 1
            
            i += 1
        return max(max_length, cur_streak)
                
```


## 657. Robot Return to Origin

Use `Counter` from    `collections`. Added  a string `RLUD` in front in order to avoid the possibility that `moves` does not contain all of the possible moves.

```
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        s = collections.Counter('RLUD'+moves)
        return s['U']-s['D'] ==0 and s['L']-s['R']==0
        
```
##  994. Rotting Oranges

This problem turns out to be more difficult than I thought. A lesson learned is that __one cannot make a set of lists in Python.__


```
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten, fresh = self.check(grid)
        h, w = len(grid), len(grid[0])
        rotting = self.newRotting(rotten, fresh, h, w)
        time = 0
        while rotting:
            time += 1
            rotten = []
            for _ in rotting:
                fresh.remove(list(_))
                rotten.append(list(_))
            rotting = self.newRotting(rotten, fresh, h, w)
        
        if fresh != []:
            return -1
        
        return time
        
        
    def check(self, grid):
            
        rotten, fresh = [], []
        h, w = len(grid), len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    rotten.append([i,j])
                elif grid[i][j] == 1:
                    fresh.append([i,j])
        return rotten, fresh
        
    def newRotting(self, rotten, fresh, h, w):
        temp=set([])
        for e in rotten:
            i, j = e[0], e[1]
            if [i+1,j] in fresh:
                temp.add((i+1,j))
            if [i-1,j] in fresh:
                temp.add((i-1,j))
            if [i, j+1] in fresh:
                temp.add((i,j+1))
            if [i,j-1] in fresh:
                temp.add((i,j-1))
            
        return temp
```
## 661. Image Smoother

Two things to note: 1. how we constructed the `nerghbors` of a given position; 2. we have to use `copy.deepcopy()` to make a copy of `M`, the shallow copy     `copy.copy()` won't work in this case.

```
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        
        x_len = len(M)
        y_len = len(M[0]) if x_len else 0
        res = copy.deepcopy(M)
        for x in range(x_len):
            for y in range(y_len):
                neighbors = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < x_len and 0 <= _y < y_len
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res
```
## 594. Longest Harmonious Subsequence

```
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        counter = collections.Counter(nums)
        res = 0
        for i in counter:
            if i+1 in counter:
                res = max(counter[i]+counter[i+1], res)
        return res
                
        
```

## 690. Employee Importance

```
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        SUM=0
        stack =[id]
        while stack:
            x=stack.pop(0)
            for i in employees:
                if i.id == x:
                    stack = stack + i.subordinates
                    SUM += i.importance
                    break
        return SUM
```
## 24. Swap Nodes in Pairs

Standard recursive method. First swap the first two nodes, then make the link correctly.

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        elif not head.next:
            return head
        else:
            node1, node2 = head, head.next
            node3 = self.swapPairs(node2.next)
            node1.next = node3
            node2.next = node1
            return node2
```
## 22. Generate Parentheses

The construction is recursive: for `n >= 2`, we have that the possible combinations must be of the following forms:

1. Either `e+f` where `e,f` are made of `i,n-i` pairs of parenthesis, where 1<= i <= n-1
2. OR `'('+e+')'` where e are made of n-1 pairs of parenthesis.

We use a cache to store the previous results.

```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['()']
        
        cache=[[],['()']]
        
        
        
        for i in range(2,n+1):
            temp=[]
            for j in range(1,i):
                for e in cache[j]:
                    temp += [e+f for f in cache[i-j]]
            temp =  temp + ['('+e+')' for e in cache[i-1]]
            cache.append(list(set(temp)))
        
        return cache[n]
```
## 852. Peak Index in a Mountain Array

Typical binary search. 

```
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right, mid = 0, len(A)-1, len(A)//2
        while A[mid] < A[mid-1] or A[mid] < A[mid+1]:
            if A[mid] < A[mid-1]:
                right, mid = mid, (left+mid)//2
            else:
                left, mid = mid, (mid+right)//2
        
        return mid
```
## 700. Search in a Binary Search Tree


```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)
```
## 697. Degree of an Array

```
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        stats = dict([])
        for i in range(len(nums)):
            if nums[i] in stats:
                stats[nums[i]][1] = i
                stats[nums[i]][2] += 1
            else:
                stats[nums[i]] = [i,i,1]
        
        degree, shortest = 0, float('inf')
        for i in stats:
            if degree == stats[i][2]:
                degree = stats[i][2]
                shortest = min(shortest, stats[i][1]-stats[i][0]+1)
            if degree < stats[i][2]:
                degree = stats[i][2]
                shortest = stats[i][1]-stats[i][0]+1
        return shortest
```
##  530. Minimum Absolute Difference in BST

(Space O(n), Time O(n)) In-order traverse the BST and record the values, which leads to a sorted list. Then find the minimal difference among the list elements.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        L = self.inOrder(root)
        return min([L[i+1]-L[i] for i in range(len(L)-1)])
    
    def inOrder(self,root):
        
        if not root:
            return []
        else:
            return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
```
## 448. Find All Numbers Disappeared in an Array

```
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i, num in enumerate(nums) if num > 0]
```
## 405. Convert a Number to Hexadecimal

```
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        sign = (num >= 0) - 1
        s = dict(zip([i for i in range(16)], [str(i) for i in range(10)]+['a','b','c','d','e','f']))
        
        quotient, remainder, digits = abs(num), 0, []
        while quotient > 0:
            quotient, remainder = quotient//16, quotient % 16
            digits.append(remainder)
        
        
        
        if sign == 0:
            digits = digits[::-1]
            return ''.join([s[i] for i in digits])
        else:
            digits = digits+[0]*(8-len(digits))
            i = 0
            while digits[i]==0:
                
                i += 1
            digits[i] = 16-digits[i]
            for j in range(i+1,8):
                digits[j] = 16 - digits[j] - 1
            digits = digits[::-1]
            return ''.join([s[i] for i in digits])
```
## 628. Maximum Product of Three Numbers

```
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[2])
```


## 706.Design HashMap

```
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 8
        self.size = 0
        self.data = [None] * 8
        self.ratio = float(2)/3

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if float(self.size)/self.cap >= self.ratio:
            self.cap = self.cap * 2
            new = [None] * self.cap
            for i in range(self.cap//2):
                if self.data[i] and self.data[i][1] != "tomb":
                    myhash = self.data[i][0]%self.cap
                    while new[myhash]:
                        myhash = (5*myhash+1)%self.cap
                    new[myhash] = self.data[i]
                i += 1
            self.data = new
            
        myhash = key % self.cap
        while self.data[myhash]:
            if self.data[myhash][0] == key:
                self.data[myhash][1] = value
                return
            
            myhash = (5*myhash+1)%self.cap
        self.data[myhash]=[key, value]
        self.size += 1
        
            
                        
                
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        myhash = key % self.cap
        while self.data[myhash]:
            if self.data[myhash][0] == key and self.data[myhash][1]=="tomb":
                return -1
            elif self.data[myhash][0] == key and self.data[myhash][1] != "tomb":
                return self.data[myhash][1]
            else:
                myhash = (5*myhash+1) % self.cap
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        myhash = key % self.cap
        while self.data[myhash]:
            if self.data[myhash][0] == key and self.data[myhash][1]=="tomb":
                return 
            elif self.data[myhash][0] == key and self.data[myhash][1] != "tomb":
                self.data[myhash][1] = "tomb"
                return
            else:
                myhash = (5*myhash+1) % self.cap


```

## 599. Minimum Index Sum of Two Lists
```
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {e:i for i, e in enumerate(list1)}
        min_sum =  len(list1)+len(list2)
        res =[]
        for i, e in enumerate(list2):
            if e in dic1:
                
                
                if i + dic1[e] ==  min_sum:
                    res.append(e)
                elif i + dic1[e] < min_sum:
                    res, min_sum = [e], i + dic1[e]
                else:
                    continue
        return res
```
## 50. Pow(x, n)

[Link](https://leetcode.com/problems/powx-n/)

```
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x, n = 1/x, -n
        
        
        res = 1
        
        if n % 2 == 1:
            
            return x* self.myPow(x*x, (n-1)//2)
        
        else:
            return self.myPow(x*x, n//2)
            
```
## 257. Binary Tree Paths

[Link](https://leetcode.com/problems/binary-tree-paths/)

Use DFS to traverse the tree. In the stack, we also keep the path from the root to the current node for output reasons.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res, stack = [], [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path+str(node.val))
            else:
                if node.left:
                    stack.append((node.left, path+str(node.val)+'->'))
                if node.right:
                    stack.append((node.right, path+str(node.val)+'->'))
        return res
```
## 401. Binary Watch
[Link](https://leetcode.com/problems/binary-watch/)

```
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        
        for hour in range(12):
            n1=self.binarydigitSum(hour)
            n2 = num - n1
            for minute in range(60):
                if self.binarydigitSum(minute) == n2:
                    res.append(str(hour)+':'+('0'+str(minute))[-2:])
        return res
        
    def binarydigitSum(self, n):
        sum = 0
        while n > 0:
            sum, n = sum + n%2, n//2
        return sum
```
## 771. Jewels and Stones

[Link](https://leetcode.com/problems/jewels-and-stones/)

```
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum = 0
        for l in J:
            
            sum += S.count(l)
        return sum
```


One-liner using `map`:

```
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(S.count, J))   

```
## 961. N-Repeated Element in Size 2N Array
[Link](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)

```
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        for i in range(len(A)-2):
            if A[i] == A[i+1] or A[i] == A[i+2]:
                return A[i]
        return A[-1]
```
## 1002. Find Common Characters

[Link](https://leetcode.com/problems/find-common-characters/)
```
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        a = set(A[0])
        dic = {e:A[0].count(e) for e in a}
        
        for e in A:
            for letter in a:
                dic[letter] = min(dic[letter], e.count(letter))
        
        res=''
        for e in dic:
            res += e * dic[e]
        return list(res)
```


Same idea, but using `collections.Counter`:

```
    def commonChars(self, A):
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())
```

## 1025. Divisor Game
[Link](https://leetcode.com/problems/divisor-game/)

```
class Solution:
    def divisorGame(self, N: int) -> bool:
        cache = [0, False, True, False] #initial cases. The 0th element is just a place-holder.
        
        i = 4
        while i <= N:
            j = 1
            sqrt = math.floor(math.sqrt(i))
            
            #If Alice can choose a strategy to ensure that Bob will lose, then she is going to win.
            
            while j <= sqrt:
                if i % j == 0 and cache[i-j]==False: 
                    
                    break
                else:
                    j += 1
            if j < sqrt:
                cache.append(True)
            else: 
                cache.append(False)
            i += 1
        return cache[N]
```

After saw other's discussion, I realize that this is a typical dynamic programming problem. Below is the more concise code, idea is exactly the same as the previous solution.

```
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False]*(N+1)
        
        i = 2
        while i <= N:
            j = 1
            sqrt = math.floor(math.sqrt(i))
            while j <= sqrt:
                if i % j == 0 and dp[i-j]==False:
                    dp[i] = True
                    break
                j += 1
            i += 1
                
        return dp[N]
```

## 720. Longest Word in Dictionary
[Link](https://leetcode.com/problems/longest-word-in-dictionary/)


```
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        w_set, res = set(['']), ''
        for word in words:
            if word[:-1] in w_set:
                w_set.add(word)
                if len(word) > len(res):
                    res = word
        return res
```

## 884. Uncommon Words from Two Sentences
[Link](https://leetcode.com/problems/uncommon-words-from-two-sentences/)

Note that want all the words which only appear once in the combination of the two sentences. This is my original code:
```
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        A_words, B_words = A.split(' '), B.split(' ')
        A_dic, B_dic = Counter(A_words), Counter(B_words)
        A_uniq, B_uniq, A_dup, B_dup = set([]), set([]), set([]), set([])
        for word in A_dic:
            if A_dic[word] == 1:
                A_uniq.add(word)
            else:
                A_dup.add(word)
        for word  in B_dic:
            if B_dic[word] == 1:
                B_uniq.add(word)
            else:
                B_dup.add(word)
        return list((A_uniq | B_uniq) - ((A_uniq | A_dup) & (B_uniq | B_dup)))
```
Below is the __smart__ code...


```
def uncommonFromSentences(self, A, B):
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]
```

## 746. Min Cost Climbing Stairs
[Link](https://leetcode.com/problems/min-cost-climbing-stairs/)


```
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] *  len(cost)
        level = 2
        while level < len(cost):
            dp[level] = min(dp[level-1]+cost[level-1], dp[level-2]+cost[level-2])
            level += 1
        return min(dp[-2]+cost[-2], dp[-1]+cost[-1])
```

Here is a DP method without using an array to store the previous costs:

```
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l<=1:
            return 0
        
        cost0, cost1 = cost[0], cost[1] 
        
        for i in range(2, l):
            cost0, cost1 = cost1, min(cost0, cost1)+cost[i]
        return min(cost0, cost1)
```

## 338. Counting Bits

[Link](https://leetcode.com/problems/counting-bits/)


```
res = [0]
        while len(res) <= num:
            res += [i + 1 for i in res[:num + 1 - len(res)]]
        return res
```
It turns out to be a DP problem! We start with `res=[0]` since the binary representation of 0 is 0, thus no 1 there. Each step, we multiply the size of `res` list by 2, and note that the numbers in the second half can be obtained by adding 1 to the corresponding numbers in the first half. Note we may compute more than we need.
```
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        if num > 0:
            
            while len(res) < num + 1:
                res += [x+1 for x in res]
        
        return res[0:num+1]
```
## 64. Minimum Path Sum
[Link](https://leetcode.com/problems/minimum-path-sum/)

```
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        for i in range(1, n_col):
            grid[0][i] += grid[0][i-1]
        for j in range(1, n_row):
            grid[j][0] += grid[j-1][0]
        
        for i in range(1, n_row):
            for j in range(1, n_col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
```
## 929. Unique Email Addresses

[Link](https://leetcode.com/problems/unique-email-addresses/)

```
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        return len(set([self.simplify(e) for e in emails]))
        
    def simplify(self, S):
        ## Return the address for string S without '.' and '+' in the local name
        
        n = S.find('@')
        first_half = S[:n]
        m = first_half.find('+') # locate the first '+' before @
        if m > -1:
            first_half = first_half[:m] # remove the part after '+' if there is one
            
        first_half = first_half.replace('.','') # remove the periods
        return first_half + S[n:]
        
```
## 836. Rectangle Overlap
[Link](https://leetcode.com/problems/rectangle-overlap/)

```
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ## first check whether there is nontrivial horizontal overlap:
        
        h1 = (rec1[0] <= rec2[0]) & (rec2[0] < rec1[2])
        h2 = (rec2[0] <= rec1[0]) & (rec1[0] < rec2[2])
        
        ## check whether there is nontrivial vertical overlap:
        
        v1 = (rec1[1] <= rec2[1]) & (rec2[1] < rec1[3])
        v2 = (rec2[1] <= rec1[1]) & (rec1[1] < rec2[3])
        return (h1 or h2) and (v1 or v2)
```

## 748. Shortest Completing Word

```
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        t = licensePlate.lower()
        L = dict()
        for i in range(ord('a'), ord('z')):
            if chr(i) in t:
                L[chr(i)] = t.count(chr(i))
        res, length = '', 1001
        for word in words:
            complete = True
            for letter in L:
                if word.count(letter) < L[letter]:
                    complete = False
                    continue
            if complete == True and len(word) < length:
                res, length = word, len(word)
        
        return res
```
## 811. Subdomain Visit Count
[Link](https://leetcode.com/problems/subdomain-visit-count/)


```
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import Counter
        dic, res = Counter(), []
        for entry in cpdomains:
            n, domain = int(entry[:entry.find(' ')]), entry[entry.find(' ')+1:]
            dic[domain] += n
            loc = domain.find('.')
            while loc != -1:
                dic[domain[loc+1:]] += n
                loc = domain.find('.', loc+1)
                
        
        return return [str(dic[e]) + ' ' + e for e in dic]
```
## 453. Minimum Moves to Equal Array Elements
[Link](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)

__Incrementing n-1 elements by 1 is effectively the same as subtracting 1 from a single element. __

```
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)
```
## 868. Binary Gap
[Link](https://leetcode.com/problems/binary-gap/)

Typical question about binary representations, we use __long division__ for that.

```
class Solution:
    def binaryGap(self, N: int) -> int:
        q, r = N // 2, N % 2
        
        # Find first 1 in the representation
        
        while r == 0:
            q, r = q//2, q%2
        
        # Keep track of distance and current max distance: whenever we encounter a 1 again, we update Max reset cnt.
        
        cnt, Max = 0, 0
        while q > 0:
            q, r, cnt = q//2, q%2, cnt + 1
            if r == 1:
                Max = max(cnt, Max)
                cnt = 0      
        return Max
```

## 1108. Defanging an IP Address
[Link](https://leetcode.com/problems/defanging-an-ip-address/)

```
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
```

## 1021. Remove Outermost Parentheses
[Link](https://leetcode.com/problems/remove-outermost-parentheses/)

```
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        net, res, start = 0 , '', 0
        for i in range(len(S)):
            
            if S[i] == '(':
                net += 1
            else:
                net -= 1
            
            if net == 0:
                res += S[start+1:i]
                start = i + 1
        return res
```

## 804. Unique Morse Code Words
[Link](https://leetcode.com/problems/unique-morse-code-words/)

```
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code_set, cnt = set(), 0
        dic = dict(zip([chr(i) for i in range(ord('a'),ord('z')+1)],[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        for word in words:
            temp = ''
            for letter in word:
                temp += dic[letter]
            if temp not in code_set:
                cnt += 1
                code_set.add(temp)
        return cnt
```

## 844. Backspace String Compare
[Link](https://leetcode.com/problems/backspace-string-compare/)

Time: O(N), Space O(N).

```
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        outS, outT = self.process(S), self.process(T)
        return outS == outT
        
    def process(self, A):
        out = []
        for i in range(len(A)):
            
            if A[i] != '#':
                out.append(A[i])
            else:
                if len(out) > 0:
                    out = out[:-1]
        return out
```
There is a way to backward checking which is Time O(N) and Space O(1):

```
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        si, ti = len(S) - 1, len(T) - 1
        count_s = count_t = 0
        
        while si >= 0 or ti >= 0:
            # si stops at non-deleted character in S or -1
            while si >= 0:
                if S[si] == '#':
                    count_s += 1
                    si -= 1
                elif S[si] != '#' and count_s > 0:
                    count_s -= 1
                    si -= 1
                else:
                    break
            
            # ti stops at non-deleted character in T or -1
            while ti >= 0:
                if T[ti] == '#':
                    count_t += 1
                    ti -= 1
                elif T[ti] != '#' and count_t > 0:
                    count_t -= 1
                    ti -= 1
                else:
                    break
            
            
            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                # eg. S = "a#", T = "a" 
                return False
            if (ti >= 0 and si >= 0) and S[si] != T[ti]:
                return False
            
            si -= 1
            ti -= 1
        return True


```

## 532. K-diff Pairs in an Array
[Link](https://leetcode.com/problems/k-diff-pairs-in-an-array/)

```
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        
        t, res = Counter(nums), 0
        
        
        
        for i in t:
            if (k>0 and i+k in t) or (k==0 and t[i]>1):
                res += 1
            
        return res
```
## 925. Long Pressed Name
[Link](https://leetcode.com/problems/long-pressed-name/)

```
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, l1, l2, cnt1, cnt2 = 0, 0, len(name), len(typed), 0, 0
        while i < l1 and j<l2:
            while i+1 < l1 and name[i] == name[i+1]:
                cnt1 += 1
                i += 1
            while j+1 < l2 and typed[j] == typed[j+1]:
                cnt2 += 1
                j += 1
            if name[i] == typed[j] and cnt1 <= cnt2:
                cnt1, cnt2, i, j = 0, 0, i+1, j+1
            else:
                return False
        return i == l1 and j == l2
```

## 860. Lemonade Change
[Link](https://leetcode.com/problems/lemonade-change/)

```
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
                i += 1
            elif bills[i] == 10:
                five, ten = five - 1, ten + 1
                if five < 0 or ten < 0:
                    return False
            
            elif bills[i] == 20:
                if ten > 0:
                    five, ten = five - 1, ten - 1
                else:
                    five -= 3
                if five < 0:
                    return False
        return True
            
```

## 944. Delete Columns to Make Sorted
[Link](https://leetcode.com/problems/delete-columns-to-make-sorted/)


```
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        cnt, m, n = 0, len(A), len(A[0])
        if m == 1:
            return True 
        
        for i in range(n):
            for j in range(m-1):
                if A[j][i] > A[j+1][i]:
                    cnt += 1
                    break
                  
        return cnt            
```

## 561. Array Partition I
[Link](https://leetcode.com/problems/array-partition-i/)



```
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i%2 == 0:
                res += nums[i]
        return res
```
## 461. Hamming Distance
[Link](https://leetcode.com/problems/hamming-distance/)



An easy application of the __bitwise XOR__ `^` operator.
```
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c, res= x^y, 0
        while c > 0:
            res, c = res+c%2, c//2
        return res
```
## 1046. Last Stone Weight
[Link](https://leetcode.com/problems/last-stone-weight/)

This is the first time using (minimal) __heap__ in Python. Take a look at the documentation about [heapq](https://docs.python.org/3/library/heapq.html).

```
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-i for i in stones]
        heapq.heapify(hp)
        for i in range(len(stones)-1):
            max1, max2 = -heapq.heappop(hp), -heapq.heappop(hp)
            heapq.heappush(hp,max2-max1)
        
        return -heapq.heappop(hp)
            
```


## 1029. Two City Scheduling

[Link](https://leetcode.com/problems/two-city-scheduling/)

```
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        return sum([x[0] for x in costs[:len(costs)//2]]) + sum([x[1] for x in costs[len(costs)//2:]])
```


## 1005. Maximize Sum Of Array After K Negations
[Link](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)

An O(NlnN) solution:
```
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        neg, zero, res, l = 0,0,0,len(A)
        A.sort()
        for i in range(l):
            temp = A[i]
            if temp < 0:
                neg += 1
            elif temp == 0:
                zero += 1
            res += temp
        
        
        for i in range(min(K,neg)):
            res += -2*A[i]
        
        if neg < K and zero == 0 and (K-neg)%2 == 1:
            if neg>0:
                
                res += max(-2*A[neg], 2*A[neg-1])
            if neg == 0:
                res += -2*A[neg]
            
        return res
                
```

Here is a O(N) solution:

```
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        c = collections.Counter(A)
        for i in range(-100, 0):
            if i in c:
                
                if K == 0:
                    break
                flips = min(K, c[i])
                c[i] -= flips
                c[-i] += flips
                K -= flips
        return sum(c.elements()) - K % 2 * min([abs(i) for i in c.keys()]) * 2
                
```

## 11. Container With Most Water
[Link](https://leetcode.com/problems/container-with-most-water/)


```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #initiate with two pointers on the left and right and the current max volumn of water
        i, j, vol = 0, len(height)-1, 0  
        
        
        while i < j:
            vol = max(vol, (j-i) * min(height[j],height[i]))
            
            # if we want to reduce the width and hope the volumn will increase, have to move the smaller height
            
            if height[i] < height[j]:    
                i += 1
            elif height[j] < height[i]:
                j -= 1
                
            # if the two heights are equal, we need to make sure we choose the proper one to move
            
            else:
                if height[i+1] >= height[j-1]:
                    j -= 1
                else:
                    i += 1
        return vol
```
## 12. Integer to Roman
[Link](https://leetcode.com/problems/integer-to-roman/)

```
class Solution:
    def intToRoman(self, num: int) -> str:
        l = [[1000, 'M'],[900,'CM'],[500, 'D'],[400, 'CD'],[100,'C'],[90,'XC'], [50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
        res = ''
        for i in range(len(l)):
            while num >= l[i][0]:
                num -= l[i][0]
                res += l[i][1]
        return res
            
```
## 5. Longest Palindromic Substring
[Link](https://leetcode.com/problems/longest-palindromic-substring/)

To take away: __how to identify palindromes given a center.__

```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # odd case:
            temp = self.helper(s, i, i)
            if len(temp) > len(res): res = temp
            
            # even case
            temp= self.helper(s,i,i+1)
            if len(temp) > len(res): res = temp
        return res
        
    def helper(self, S, l, r):
        # Return the longest palindrom in S which is centered at (l,r)-location.
        # l==r correspondes to the odd case and r==l+1 correspond to the even case
        
        while l >= 0 and r < len(S) and S[l]==S[r]:
            l, r = l-1, r+1
        return S[l+1:r]
```
## 6. ZigZag Conversion
[Link](https://leetcode.com/problems/zigzag-conversion/)

```
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1:
            return s
            
        # Split the ZigZag into small pieces, and put each letter into the corresponding row
        new, l, r, k = ['' for i in range(numRows)], 0, 2*numRows-2, numRows
        temp = s[l:r]
        while temp != '':
            for i in range(k):
                if i==0 or i==k-1:
                    new[i] += temp[i:i+1]
                else:
                    new[i] += temp[i:i+1]
                    new[i] += temp[2*k-i-2:2*k-i-1]
            l, r = l+2*k-2, r+2*k-2
            temp = s[l:r]
        return ''.join(new)
```
## 8. String to Integer (atoi)
[Link](https://leetcode.com/problems/string-to-integer-atoi/)

```
class Solution:
    def myAtoi(self, str: str) -> int:
        i, res = 0, ''
        while i<len(str) and str[i] == ' ':
            i += 1
        
        if i >= len(str) or str[i] not in '+-0123456789':
            return 0
        else:
            res += str[i]
            i += 1
            while i < len(str) and str[i] in '0123456789':
                res += str[i]
                i += 1
            
            if res == '+' or res == '-':
                return 0
            
            res = int(res)
            if res < -2**31:
                return -2**31
            elif res > 2**31-1:
                return 2**31-1
            else:
                return res
```

## 10. Regular Expression Matching
[Link](https://leetcode.com/problems/regular-expression-matching/)

This one is very hard. The DP approach is the hardest DP problem I've seen so far. __One key assumption__, which to me is necessary but not explicitly mentioned, is that in `p`, there will not be any `*`s appearing consectively.

```
class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]
```

## 29. Divide Two Integers
[Link](https://leetcode.com/problems/divide-two-integers/)

```
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        
        if dividend == 0:
            return 0
        
        sign, res = 1, 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor >0):
            sign = -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        if divisor == 1:
            res = dividend
        else:
        
            temp = [[divisor,1]]
            for _ in range(32):
                a,b = temp[-1][0]+temp[-1][0], temp[-1][1]+temp[-1][1]
                temp.append([a,b])

            while dividend >= divisor:
                i = 32
                while i >= 0:
                    while dividend >= temp[i][0]:
                        dividend = dividend - temp[i][0]
                        res += temp[i][1]
                    i -= 1
        
        res = sign * res
        
        if res < -2**31 or res > 2**31 - 1:
            return 2**31-1
        else:
            return res
        
        
```

## 17. Letter Combinations of a Phone Number
[Link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return list(dic[digits])
        
        prev = self.letterCombinations(digits[:-1])
        temp = list(dic[digits[-1]])
        return [s+t for s in prev for t in temp]
```


## 232. Implement Queue using Stacks
[Link](https://leetcode.com/problems/implement-queue-using-stacks/)


Use two stacks to implement. `push` O(1), 'pop' amortized O(1).

```
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.istack = []
        self.outstack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.outstack == []:
            while self.instack:
                self.outstack.append(self.instack.pop())
        
        if self.outstack == []:
            return 'Nothing there!'
        else:
            return self.outstack.pop()
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.outstack == []:
            while self.instack:
                self.outstack.append(self.instack.pop())
        
        if self.outstack == []:
            return 'Nothing there!'
        else:
            return self.outstack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.instack == [] and self.outstack == []
```
## 18. 4Sum
[Link](https://leetcode.com/problems/4sum/)

In the solution, we actually defined the method to find general N-sum for any N >= 2. The core part is to defined 2Sum, which is O(N) time. Then we recursively reduce to the 2Sum case. Thus the time complexity is O(N^3).

```
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.N_sum(nums, target, 4, [], res)
        return res
    
    def N_sum(self, nums, target, N, temp, res):
        if N < 2 or len(nums) < N:
            return
        
        elif N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l]+nums[r] == target:
                    res.append(temp+[nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                
                elif  nums[l] + nums[r] < target:
                    l += 1
                
                else:
                    r -= 1
            return
        
        else:
            for i in range(len(nums)-N+1):
                if nums[i]*N > target or nums[-1]*N < target:
                    break
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    self.N_sum(nums[i+1:], target - nums[i], N-1, temp+[nums[i]], res)
            return 
```
## 19. Remove Nth Node From End of List
[Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

This is a typical technique in dealing with linked lists: using a fast and a slow pointer.

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
            
        # if the n-th node from the end is the head (since we know n will always be valid)    
        if not fast:
            return head.next
        
        # when fast reach the end, slow is at the n-th position
        while fast.next:
            fast, slow = fast.next, slow.next
        
        # skip the n-th
        slow.next = slow.next.next
        return head
```
## 31. Next Permutation
[Link](https://leetcode.com/problems/next-permutation/)

This solution actually is not in place, but we can achieve that by sorting `nums[left+1:]' in place.

```
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Initiate: left is the right most index i where nums[i]<nums[i+1]. If such an i exists, we mark `possible`
        # to be True, which indicates that the next permutation is possible. `Right` is the largest index i where           # nums[j]>nums[left] and nums[j] >= nums[j+1] for all j such that left+1 <= j <= i+1.
        # Once left and right are found, we swap nums[left] and nums[right], and then sort nums[left+1:] in place.
        
        i, left, right, possible = 0, 0, 0, False
        while i < len(nums)-1:
            if nums[i] >= nums[i+1]: 
                i += 1
            else:
                left, right, possible = i, i+1, True
                i += 1
                while i < len(nums)-1 and nums[i] >= nums[i+1] and nums[i+1] > nums[left]:
                    right = i+1
                    i += 1
        if possible:
            nums[left], nums[right] = nums[right], nums[left]
            t=nums[left+1:]
            t.sort()
            nums[left+1:]=t
        else:
            self.reverse(nums, 0, len(nums)-1)
            
    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
```
## 36. Valid Sudoku
[link](https://leetcode.com/problems/valid-sudoku/)

```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_rows(board):
            
            for i in range(9):
                s=[]
                for j in range(9):
                    if board[i][j] != '.':
                        s.append(board[i][j])
                if len(s) != len(set(s)):
                    return False
            return True
        
        def check_cols(board):
            return check_rows(list(zip(*board)))
        
        def check_box(board, m, n):
            s=[]
            for i in range(3):
                
                for j in range(3):
                    if board[m+i][n+j] != '.':
                        s.append(board[m+i][n+j])
            if len(s) != len(set(s)):
                return False
            
        def check_all_boxes(board):
            for m in [0,3,6]:
                for n in [0,3,6]:
                    if check_box(board,m,n)==False:
                        return False
            return True
        
        return check_rows(board) and check_cols(board) and check_all_boxes(board)
```
## 46. Permutations
[Link](https://leetcode.com/problems/permutations/)

Recursive solution:

```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        else:
            res =[]
            for i in range(len(nums)):
                res += [[nums[i]]+e for e in self.permute(nums[:i]+nums[i+1:])]
            return res
```

__Iterative solution:__
```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            new = []
            for l in res:
                for j in range(len(l)+1):  # Here len(l)+1 to ensure we insert n after l
                    new.append(l[:j]+[n]+l[j:])
            res = new
        return res
           
```

## 47. Permutations II

__Recursive solution.__ Since lists are not hashable in `Python`, we have to check whether a permutation is already contained in the res or not before adding it. This greatly slows down the solution.

```
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        else:
            res =[]
            for i in range(len(nums)):
                for e in self.permuteUnique(nums[:i]+nums[i+1:]):
                    if [nums[i]]+e not in res:
                        res.append([nums[i]]+e)
                
            return res

```

__Iterative solution.__ Just adding one line to deal with the duplicate situation.

```
Class Solution:
	def permuteUnique(self, nums):
		res = [[]]
		for n in nums:
			new =[]
			for l in res:
				for i in range(len(l)+1):
					new.append(l[:i]+[n]+l[i:])
					# Deal with duplicate
					if i<len(l) and n==l[i]:  
						break
			res = new
		return res
```

## 62. Unique Paths
[Link](https://leetcode.com/problems/unique-paths/)

Just basic combinatorics.

```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        K, k = m+n-2, min(m,n)-1
        numerator, denom = 1, 1
        for i in range(1,k+1):
            numerator *= (K-i+1)
            denom *= i
        return numerator//denom
````



## 213. House Robber II
[Link](https://leetcode.com/problems/house-robber-ii/)

````
class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        # Some easy edge cases
        if L == 0:
            return 0
        elif L == 1:
            return nums[0]
        elif L <= 3:
            return max(nums)
        
        else:
            res1 = self.rob_no_circ(nums[2:L-1])+nums[0]
            res2 = self.rob_no_circ(nums[1:])
            return max(res1, res2)
        
    def rob_no_circ(self, houses):
        # This function take a list of numbers and return the max amount a robber 
        # can get by loosing on the circle restriction. 
        if len(houses) <= 2:
            return max(houses)
        # Assuming len(houses)>2
        # dp[i] represents the max amount if the robber just robs the first i-houses
        dp = [0]*(len(houses)+1)
        dp[1] = houses[0] 
        for i in range(2, len(houses)+1):
            dp[i] = max(dp[i-2]+houses[i-1], dp[i-1])
        return dp[-1]
````
## 34. Find First and Last Position of Element in Sorted Array
[Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)


```
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Idea: use binary search three times: the first time to check whether 
        # target is in the list or not, if its there, return left, mid, right at the
        # last step of the search; the 2nd and 3rd search is to locate the first and 
        # the last appearance of target.
        
        
        
        def binarySearch(nums, target):
            # Binary search: if target not there, return -1; 
            # otherwise return left, mid, right of the last step for the search. 
            # Note that nums[mid]==target.
            
            left, right = 0, len(nums)-1
            if not nums:
                return -1
            while left+1 < right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return left, mid, right
                elif nums[mid] < target:
                    left = mid
                else:
                    right = mid
            if nums[left] == target:
                return left, left, right
            elif nums[right] == target:
                return left, right, right
            else:
                return -1
        
        def leftSearch(nums, target, left, right):
            # Binary search to find the starting position 
            # if nums[left-1] < target and nums[right] == target
            if nums[left] == target:
                return left
            else:
                mid = (left+right)//2
                if nums[mid] < target:
                    return leftSearch(nums, target, mid+1, right)
                else:
                    return leftSearch(nums, target, left, mid)
                
        def rightSearch(nums, target, left, right):
            # Binary search to find the ending position 
            # if nums[right+1] > target and nums[left] == target
            if nums[right] == target:
                return right
            else:
                mid = (left+right)//2 + 1
                if nums[mid] > target:
                    return rightSearch(nums, target, left, mid-1)
                else:
                    return rightSearch(nums, target, mid, right)
        
        if binarySearch(nums, target) == -1:
            return [-1,-1]
        else:
            left, mid, right = binarySearch(nums, target)
            return [leftSearch(nums, target, left, mid),rightSearch(nums,target,mid, right)]
                
            
```

## 207. Course Schedule
[Link](https://leetcode.com/problems/course-schedule/)
```
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        
        taken = set()
        
        pre = [set() for _ in range(numCourses)]
        for e in prerequisites:
            pre[e[0]].add(e[1])
            
        nxt = set()
        for i in range(numCourses):
            if pre[i] == set():
                nxt.add(i)
        
        while nxt:
            taken = taken.union(nxt)
            nxt = set()
            for i in range(numCourses):
                if i not in taken and len(pre[i]-taken)==0:
                    nxt.add(i)
        return len(taken)==numCourses            
```
## 210. Course Schedule II

```
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if numCourses == 0:
            return True
        
        taken = []
        
        pre = [set() for _ in range(numCourses)]
        for e in prerequisites:
            pre[e[0]].add(e[1])
            
        nxt = []
        for i in range(numCourses):
            if len(pre[i]) == 0:
                nxt.append(i)
        
        while nxt:
            taken = taken + nxt
            nxt = []
            taken_set = set(taken)
            for i in range(numCourses):
                if i not in taken_set and len(pre[i]-taken_set)==0:
                    nxt.append(i)
        if len(taken) == numCourses:
            return taken
        else:
            return []
```
## 39. Combination Sum
[Link](https://leetcode.com/problems/combination-sum/)

```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, ind, path, res):
        if target == 0:
            res.append(path)
            return 
        else:
            for i in range(ind, len(nums)):
                if nums[i] > target:
                    break
                self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
```

## 40. Comnination Sum II

- The main difference is that we can only use each number in the `candidates` list at most once in each combination. To achieve that, each time to recursive call the helper function, we need to increase the starting index by 1.
- Another subtle point is that due to the possibility that the `candidates` list may contain repetitions, we need to address potential repetitions in our output. A slow but easier way whenever we want to append a combination to the output, we check whether it is already in it; a faster way is that in the `for` loop of the helper function, we make sure that we omit all the cases in which `i > ind and nums[i]==nums[i-1]`.

Approach 1 (slower):

```
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs_noRepeat(candidates, target, 0, [], res)
        return res
    
    def dfs_noRepeat(self, nums, target, ind, path, res):
        if target == 0:
            if path not in res:     # Avoiding repeatitions
                res.append(path)
            return 
        else:
            for i in range(ind, len(nums)):
                if nums[i] > target:
                    break
                self.dfs_noRepeat(nums, target-nums[i], i+1, path+[nums[i]], res)  # note that we use i+1 for the recursive call to ensure that we are never using the same number twice
```

Approach 2 (faster):

```
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs_noRepeat(candidates, target, 0, [], res)
        return res
    
    def dfs_noRepeat(self, nums, target, ind, path, res):
        if target == 0:
            res.append(path)
            return 
        else:
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i-1]:  # avoiding repetitions
                    continue
                if nums[i] > target:
                    break
                self.dfs_noRepeat(nums, target-nums[i], i+1, path+[nums[i]], res)  # use i+1 for the recursive call to ensure that we are never using the same number twice
```


## 33. Search in Rotated Sorted Array

One can use Binary Search all the same, just when deciding when side to continue requires a bit thinking.

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        
        
        while l <= r:
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            mid = (l+r)//2
            if l == mid:
                return -1
            
            if nums[mid] == target:
                return mid
            
            if nums[l] < nums[mid]:   # Case 1: the first half is strictly increasing
                if target < nums[mid] and target > nums[l]:
                    l, r = l+1, mid-1
                else:
                    l, r = mid+1, r-1
            else:                     # Case 2: the first half has a 'cliff'
                if target < nums[mid] or target > nums[l]:
                    l, r = l+1, mid-1
                else:
                    l, r = mid+1, r-1
        return -1
```

## 43. Multiply Strings

Multiplying things out by defition. Updating each digits accordingly.
```
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        dic = {str(i):i for i in range(10)}
        res = [0]*(len(num1)+len(num2))   # the product is AT MOST this long
        
        for i in range(len(num1)-1, -1, -1):  # computation goes from right to left
            next_d = 0                # contribution to the next digit on the LEFT
            n1 = dic[num1[i]]         # i-th digit of num1
            for j in range(len(num2)-1,-1,-1):
                n2 = dic[num2[j]]     # j-th digit of num2
                pos = i+j+1   # the position of the product
                temp = n1*n2  # the product of the i-th and j-th digits for num1, num2
                
                res[pos], next_d = (res[pos]+temp%10+next_d)%10, temp//10 + (temp%10 + res[pos]+next_d)//10
            
            while pos-1 >= 0 and next_d > 0:   # updating the left digits
                pos -= 1
                res[pos], next_d = (res[pos]+next_d)%10, (res[pos]+next_d)//10
        
        if res[0] == 0:
            return ''.join([str(res[i]) for i in range(1,len(res))])  
        else:
            return ''.join([str(res[i]) for i in range(len(res))])
```

## 48. Rotate Image

The difficult part is to change in-place. Suppose that we obtain matrix B by rotating matrix A clockwise by 90 degrees. Then a careful check can show that `B[i][j] = A[n-1-j][i]` where n is the dimension of A.

Therefore we can update each time four entries which lie in the corners of a square. A subtle point is that we only need to rotate one forth of the entire matrix. 

```
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
    
        """
        # rotate the matrix, we use the bottom left one-fourth as our axis

        n = len(matrix)
        for j in range(n//2):
            for i in range(j, n-j-1):
                self.helper(matrix, i, j , n)
        return
        
    def helper(self, matrix, i, j, n):
        """
        Rotate four entries of the matrix at the corners of a square where the left-most corner is at (i,j), where i>=j
        """
        
        matrix[i][j],matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j],
        return
```
## 49. Group Anagrams

Using sorted words from the input as keys in a dictionary. Then values are lists in the same anagram class.

```
class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))  
            d[key] = d.get(key, []) + [w]
        return list(d.values())
```

## 78. Subsets
It really feels like a DFS.
```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for i in range(len(nums)):
            res += [e+[nums[i]] for e in res]
        return res
            
```


## 63. Unique Paths II

Method 1: (O(2^(m+n))). Brute-force DFS. 
```
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        stack, res = [(0,0)], 0 
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        while stack:
            i, j = stack.pop()
            if i == m-1 and j == n-1:
                res += 1
            else:
                if i+1 < m and obstacleGrid[i+1][j] == 0:
                    stack.append((i+1,j))
                if j+1 < n and obstacleGrid[i][j+1] == 0:
                    stack.append((i,j+1))
        return res
```


Method 2: (Time O(mn), space O(mn)). DP method. One can also clean the code a bit to make it only use space O(n).


```
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
         
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] * (1-obstacleGrid[0][i])
        for j in range(1,m):
            dp[j][0] = dp[j-1][0] * (1-obstacleGrid[j][0])
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j]+dp[i][j-1]) * (1-obstacleGrid[i][j])
                
        return dp[-1][-1]

```

## 980. Unique Paths III

```
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # first locate the start and end position
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: sx, sy = i, j 
                if grid[i][j]==2: end = (i,j)
                if grid[i][j]==0: empty += 1
        
        self.res = 0
        
        def backstrack(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0): return
            
            if (x,y) == end:
                self.res +=  empty == 0
                return 
            
            grid[x][y] = -2 # mark the current position to avoid repetition
            backstrack(x-1, y, empty-1)
            backstrack(x+1, y, empty-1)
            backstrack(x, y-1, empty-1)
            backstrack(x, y+1, empty-1)
            grid[x][y] = 0 # reset
        
        backstrack(sx, sy, empty)
        return self.res
```

## 73. Set Matrix Zeroes

Method 1: Time O(mn), Space(m+n). Scan the entire matrix and record in  two lists `rows` and `cols` which rows and columns contains zeros. Then go through the matrix twice to modify.

```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = [0]*m, [0]*n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i], cols[j] = 1, 1
        
        for i in range(m):
            if rows[i] == 1:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(n):
            if cols[j] == 1:
                for i in range(m):
                    matrix[i][j] = 0
```


Method 2: Time O(mn), space O(1). Use the first row and first column to record zeros.

```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # First rowc/col has zero?
        m, n = len(matrix), len(matrix[0])
        firstRowHasZero = not all(matrix[0])
        firstColHasZero = not all([matrix[i][0] for i in range(m)])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros except for the first row and first column
        for i in range(1, m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row and first column
        if firstRowHasZero:
            matrix[0] = [0] * n
        if firstColHasZero:
            for i in range(m):
                matrix[i][0] = 0
```

## 71. Simplify Path

```
class Solution:
    def simplifyPath(self, path: str) -> str:
        # we add a '/' to the end to ensure while loop will end
        d, prev, path = [], 0,  path+'/'  
        
        while prev < len(path)-1:
            next = path.find('/', prev+1)
            word = path[prev+1: next]
            prev =  next
            if word == '.' or word == '':
                continue
            elif word == '..':
                if d: d.pop()
            else:
                d.append('/'+word)
        
        if not d: return '/'
        
        return ''.join(d)
```
## 42. Trapping Rain Water

```
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1: return 0
        # The list peaks records the locations for all local max
        peaks=[]
        if height[0] > height[1]: peaks.append(0)
            
        for i in range(1, len(height)-1):
            if (height[i] > height[i-1] and height[i] >= height[i+1]) or (height[i] >= height[i-1] and height[i] > height[i+1]):
                peaks.append(i)
        
        if height[-1] > height[-2]:
            peaks.append(len(height)-1)
        # If just 1 local max, no water can be trapped
        if len(peaks) <= 1:
            return 0
        
        # Otherwise, check whether the local max can be overshadowed from both sides
        
        left_max, right_max = [-float('inf')]*len(peaks), [-float('inf')]*len(peaks)
        for i in range(1, len(peaks)):
            left_max[i], right_max[-i-1] = max(left_max[i-1], height[peaks[i-1]]), max(right_max[-i], height[peaks[-i]])
        
        # The list levels stores all the local max which stands out as boundaries
        # for the water traps
        levels = []
        for i in range(len(peaks)):
            if height[peaks[i]] > left_max[i] or height[peaks[i]] > right_max[i]:
                levels.append(peaks[i])
        
        res = 0
        for i in range(len(levels)-1):
            left, right = levels[i], levels[i+1]
            # Choose the lowest side as the height of the bucket
            level = min(height[left],height[right])
            
            # Add the water in the bucket to the total amount
            # Need to ignore those whose height exceeds the height of the bucket
            for j in range(left+1, right):
                if height[j] > level:
                    j += 1
                else:
                    res += (level-height[j])
        return res 
```

## 54. Spiral Matrix

Time O(mn), Space O(1).

```
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        m, n, res = len(matrix), len(matrix[0]), []
        self.helper(matrix, 0, m, n, res)
        return res
    
    def helper(self, M, k, m, n, res):
        '''
        The helper will record the k-th (starting from 0 th) rectanglular outskirt layer of the  matrix M of size m*n where the top left corner is located at (k,k)
        '''
        m1, n1 = m - 2*k -2, n - 2*k-2
        if min(m1, n1) < -1:
            return
        
        # if only 1 line left, add the line and end
        elif m1 == -1: 
            res += M[k][k:n-k]
            return
        
        # if only 1 col left, add the line and end
        elif n1 == -1:
            res += [M[i][k] for i in range(k,m-k)]
            return 
        
        # if we still have rectangles to run
        else:
            
            # add the top row
            res += M[k][k:n-k]
            # add the right col: j = n-k-1
            for i in range(k+1, m-k):
                res.append(M[i][n-k-1])

            # add the bottom row: i = m-k-1
            for j in range(n-k-2, k-1, -1):
                res.append(M[m-k-1][j])
            # add the left col: j = k
            for i in range(m-k-2,k,-1):
                res.append(M[i][k])

            self.helper(M, k+1, m, n, res)
```

## 59. Spiral Matrix II

```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0]*n for _ in range(n)]
        self.helper(M, 1, n, 1)
        return M
        
    def helper(self, M, k, n, s):
        '''
        Fill the k-th (outside most is the 1st) rectangular layer of an n*n matrix M.
        s is the first number we need to use.
        '''
        if s > n*n:
            return 
        
        if n%2==1 and k == n//2+1:
            M[k-1][k-1] = s
            return
        
        # fill top row: i=k-1
        for j in range(k-1, n-k+1):
            M[k-1][j] = s
            s += 1
        # fill right col: j = n-k
        for i in range(k, n-k+1):
            M[i][n-k] = s
            s += 1
        # fill bottom row: i = n-k
        for j in range(n-k-1,k-2,-1):
            M[n-k][j] = s
            s += 1
        # fill left col: j = k-1
        for i in range(n-k-1,k-1,-1):
            M[i][k-1] = s
            s += 1
        self.helper(M, k+1, n, s)
```


## 55. Jump Game

Going backwards.

```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= goal:
                goal = i
        return goal == 0
```

## 45. Jump Game II

Essentially a DFS in the guise of a greedy method.

```
class Solution:
    def jump(self, nums: List[int]) -> int:
        curFarthest, curEnd, res = 0 , 0, 0
        for i in range(len(nums)):
            
            if curEnd >=  len(nums)-1:
                return res
            curFarthest=max(curFarthest, i+nums[i])
            
            if i == curEnd:
                res += 1
                curEnd = curFarthest
```
## 94. Binary Tree Inorder Traversal

Trivial recursive method:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
```

Iterative method:
```
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            # Going all the way down to the left
            while root:
                stack.append(root)
                root = root.left
            # Return if nothing to pop
            if not stack:
                return res
            
            # From bottom left to top, pop the node, then traverse the right branch 
            node = stack.pop()
            res.append(node.val)
            if node.right:
                root = node.right         
```

## 56. Merge Intervals

```
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res,i = [], 0
    
        while i < len(intervals):
            left, right = intervals[i][0], intervals[i][1]
            next = i+1
            while next < len(intervals) and intervals[next][0] <= right:
                right, next = max(right,intervals[next][1]), next + 1
            res.append([left,right])
            i = next
        return res
```
## 57. Insert Interval

```
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if intervals[-1][1] < newInterval[0]:
            return intervals+[newInterval]
        res, i = [], 0
        newLeft, newRight = newInterval[0], newInterval[1]
        while i < len(intervals):
            if intervals[i][1] < newLeft:
                i += 1
            else:
                res += intervals[:i]
                if intervals[i][0] > newRight:
                    res.append(newInterval)
                    return res + intervals[i:]
                
                newLeft = min(newLeft, intervals[i][0])
                newRight = max(newRight, intervals[i][1])
                
                i += 1
                while i < len(intervals) and newRight >= intervals[i][0]:
                    newRight = max(newRight, intervals[i][1])
                    i += 1
                res.append([newLeft, newRight])
                res += intervals[i:]
                break
        return res
```

## 60. Permutation Sequence

Equivalently, present any number `k` in the 'n-factorial' system.

```
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        res, nums, r = '', [i for i in range(1,n+1)], k-1 # r starts with k-1 since we are using the residual method
        factorial = 1
        for i in range(1,n):
            factorial *= i
        
        # Long division in the 'n-factorial' setting. Remember to pop the numbers that have been used before.

        for i in range(1,n):
            q, r = int(r//factorial), r%factorial
            res += str(nums.pop(q))
            factorial = factorial/(n-i)
            
        res += str(nums[0])
        return res
```

## 61. Rotate List

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        # Find the total length of the linked list
        l, node = 1, head
        while node.next:
            l += 1
            node = node.next
               
        # link the tail with the head to form loop
        k, tail = k%l, node 
        tail.next = head
        
        # find the new head
        prev, cur = tail, head
        for i in range(l-k):
            prev, cur = cur, cur.next
        
        prev.next, head = None, cur
        
        return head
```
## 96. Unique Binary Search Trees

Typical DP. Once we chose the root value as `k`, where `1<= k <= n`, then the left subtree must have `k-1` nodes and the right subtree must have `n-k` nodes.
```
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        
        dp[1], dp[0] = 1, 1
        
        for i in range(2, n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        
        return dp[-1]
```

## 97. Unique Binary Search Trees II

I still need practicing on DFS.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return self.dfs(1,n)
    
    def dfs(self, start, end):
        if start > end:
            return [None]
        
        res = []
        for i in range(start, end+1):
            for l in self.dfs(start, i-1) or [None]:
                for r in self.dfs(i+1, end) or [None]:
                    root = TreeNode(i)
                    root.left, root.right = l, r
                    res.append(root)
        return res
```

## 443. String Compression

Turns out to be really subtle for me.

```
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)
        
        
        cur, cnt, i = chars[0], 1, 1
        
        while i < len(chars):
            
            while i < len(chars) and chars[i] == cur:
                cnt += 1
                chars.pop(i)
            if cnt > 1:
                s = str(cnt)
                for j in range(len(s)-1,-1,-1):
                    chars.insert(i, s[j])
                if i+len(s) < len(chars):
                    cur, cnt = chars[i+len(s)], 1
                i += len(s)+1
            else:
                cur = chars[i]
                i += 1
        return len(chars)
```

## 51. N-Queens

DFS exploration, still need to practice more.
```
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.dfs(n,[],[],[])
        return [['.'*(i-1) +'Q' + '.'*(n-i) for i in path] for path in self.res]
        
    def dfs(self, n, xy_sum, xy_dif, path):
        if len(path) == n:
            self.res.append(path)
            return 
        
        x = len(path)
        for y in range(1, n+1):
            if y not in path and x+y not in xy_sum and x-y not in xy_dif:
                self.dfs(n, xy_sum+[x+y],xy_dif+[x-y], path+[y])

```
## 52. N-Queens II

```
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.dfs(n,[],[],[])
        return self.res
        
    def dfs(self, n, xy_sum, xy_dif, path):
        if len(path) == n:
            self.res += 1
            return 
        
        x = len(path)
        for y in range(1, n+1):
            if y not in path and x+y not in xy_sum and x-y not in xy_dif:
                self.dfs(n, xy_sum+[x+y],xy_dif+[x-y], path+[y])
```
## 74. Search a 2D Matrix

```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m-1, 0, n-1
        
        # Binary search for row number
        if matrix[top][0] > target or matrix[bottom][-1] < target:
            return False
        
        while top < bottom:
            mid = (top+bottom)//2
            if matrix[bottom][0] <= target:
                i = bottom
                break
            elif matrix[top][-1] >= target:
                i = top
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top, bottom = mid, bottom - 1
        if top == bottom:
            i = top
        if top > bottom: 
            return False
        
        # Binary search for col number
        if matrix[i][left] > target or matrix[i][right] < target:
            return False
        
        while left <= right:
            mid = (left+right)//2
            if matrix[i][left] == target or matrix[i][right] == target or matrix[i][mid] == target:
                return True
            elif matrix[i][mid] <  target:
                left = mid + 1
            elif matrix[i][mid] > target:
                right = mid - 1
        return False
```

## 240. Search a 2D Matrix II

```
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        j = -1
        for row in matrix:
            while j + len(row) and target < row[j]:
                j -= 1
            if row[j] == target:
                return True
        return False
```
## 75. Sort Colors

```
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counts of 0 and 1 appeared so far
        zero, one = 0, 0
        for i in range(len(nums)):
            val = nums[i]
            nums[i] = 2
            # if we get a new 0, add a new 0 in front. Note it may replace a previous 1, so we have to remedy
            if val == 0:
                if nums[zero] == 1:
                    nums[zero+one] = 1
                nums[zero] = 0
                zero += 1
            if val == 1:
                nums[zero+one] = 1
                one += 1
```

## 77. Combinations

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.dfs(n, [], k, 1)
        return self.res
        
    def dfs(self, n, path, k, start):
        if k==0:
            self.res.append(path)
            return
        
        for i in range(start,n+1):
            # if not enough numbers to choose from, break.
            if k > n-start+1:
                break
            
            self.dfs(n, path+[i], k-1, i+1)
```
## 80. Remove Duplicates from Sorted Array II

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 
        
        i, prev, cnt  = 1, nums[0], 1
        while i < len(nums):
            if nums[i] != prev:
                prev, i, cnt = nums[i], i+1, 1
            
            elif cnt == 2:
                nums.pop(i)
            elif cnt == 1:
                i, cnt = i+1, cnt+1
        
        return len(nums)
```
## 82. Remove Duplicates from Sorted List II

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
            
        
        prev, cur, stack, cnt = head, head.next, [], 1
        while cur:
            while cur and cur.val == prev.val:
                cur, cnt = cur.next, cnt+1
            if cnt > 1:   
                stack.append(prev.val)
                cnt = 1
            prev.next = cur
            prev = cur
            if cur:
                cur = cur.next
        
        while head and stack and head.val == stack[0]:
            stack.pop(0)
            head = head.next
            
        if head:    
            prev, node = head , head.next
            while stack:
                val = stack.pop(0)
                while node.val != val:
                    prev, node =  node, node.next
                prev.next, node = node.next, node.next
        return head
```
## 81. Search in Rotated Sorted Array II

```
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        
        while l <= r:
            if target == nums[l] or target == nums[r]:
                return True
            mid = (l+r)//2
            if l == mid:
                return False
            
            if nums[mid] == target:
                return True
            
            if nums[l] < nums[mid]:
                if target < nums[mid] and target > nums[l]:
                    l, r = l+1, mid-1
                else:
                    l, r = mid+1, r-1
            elif nums[l] > nums[mid]:
                if target < nums[mid] or target > nums[l]:
                    l, r = l+1, mid-1
                else:
                    l, r = mid+1, r-1
            # if nums[l] == nums[mid], we don't know how to do, so split and                     # consider both halves.
            else: 
                return self.search(nums[l+1:mid], target) or self.search(nums[mid+1:r],target)
                
        return False
```

## 79. Word Search

My original code: 
```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(board, i, j, word, 0, []):
                    return True
        return False
    def dfs(self, B, i, j, word, k, path):
        # Search word in the given board B starting at (i,j). Return True if able to
        # find the word[k:].
        if k >= len(word):
            return True
        m, n = len(B), len(B[0])
        if i >= m or j >= n or i<0 or j<0 or (i,j) in path:
            return False
        if B[i][j]  == word[k]:
            return self.dfs(B,i+1,j, word, k+1, path+[(i,j)]) or self.dfs(B,i,j+1, word, k+1, path+[(i,j)]) or self.dfs(B,i-1,j, word, k+1, path+[(i,j)]) or self.dfs(B,i,j-1, word, k+1, path+[(i,j)])
```

To check where `(i,j)` is in `path` or not really slow things down. Below is a slight improvement.
```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self,B, i, j, word, k):
        '''
        Search word in the given board B starting at (i,j). Return True if able to
        find the word[k:].
        '''
        if k >= len(word):
            return True
        m, n = len(B), len(B[0])
        if i >= m or j >= n or i<0 or j<0 or B[i][j]!=word[k]:
            return False
        # Here before the recursive call, we need to modify some inputs. 
        # After calling it, we will change inputs back
        temp = B[i][j]
        B[i][j] = None
        res = self.dfs(B,i+1,j, word, k+1) or self.dfs(B,i,j+1, word, k+1) or self.dfs(B,i-1,j, word, k+1) or self.dfs(B,i,j-1, word, k+1)
        B[i][j] = temp
        return res
```
## 89. Gray Code


```
class Solution:
    def grayCode(self, n: int) -> List[int]:
        '''
        from up to down, then left to right

        0   1   11  110
                10  111
                    101
                    100

        start:      [0]
        i = 0:      [0, 1]  
        i = 1:      [0, 1, 3, 2]
        i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
        '''
        
        res = [0]
        for i in range(n):
            power = 2 ** i
            res += [x+power for x in res[::-1]]
        return res
```
## 90. Subsets II

```
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res
```

## 113. Path Sum II
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        self.res = []
        self.dfs(root, 0, [], sum)
        return self.res
        
    def dfs(self, root, Sum, path, target):
        if not root.left and not root.right:
            if Sum + root.val == target:
                self.res.append(path+[root.val])
                return
        
        if root.left:
            self.dfs(root.left, Sum+root.val, path+[root.val], target)
        if root.right:
            self.dfs(root.right, Sum+root.val, path+[root.val], target)
```
## 437. Path Sum III

Brute Force: Time O(n^2), where n is the number of nodes in the tree.
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0 
        
        if root:
            self.dfs(root, sum)
            if root.left:
                self.res += self.pathSum(root.left, sum)
            if root.right:
                self.res += self.pathSum(root.right, sum)
        
        return self.res
        
    def dfs(self, root, target):
        '''
        Add the number of paths starting with root with sum equal to target.
        They may not end in leaves.
        '''
        if not root:
            return 
        if root.val == target:
            self.res += 1
        if root.left:
            self.dfs(root.left, target-root.val)
        if root.right:
            self.dfs(root.right, target-root.val)
```

Using cache, O(n).

- In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the intermediate result. Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
- This is a classical 'space and time tradeoff': we can create a dictionary (named `cache`) which saves all the path sum (from root to current node) and their frequency.
- Again, we traverse through the tree, at each node, we can get the `currPathSum` (from root to current node). If within this path, there is a valid solution, then there must be a `oldPathSum` such that `currPathSum - oldPathSum` = `target`.
- We just need to add the frequency of the `oldPathSum` to the result.
- During the DFS break down, we need to -1 in `cache[currPathSum]`, because this path is not available in later traverse.

```
class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
```

## 931. Minimum Falling Path Sum

Brute Force using DFS:
```
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        self.res = float('inf')
        for j in range(len(A)):
            self.dfs(A, 0, j, len(A), 0)
        return self.res
    
    def dfs(self, M, i, j, n, Sum):
        if i == n-1:
            self.res = min(self.res, Sum+M[i][j])
            return 
        
        for k in range(-1, 2):
            if j+k >= 0 and j+k < n:
                self.dfs(M, i+1, j+k, n, Sum+M[i][j])
        
```

DP method:
```
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [A[0][j] for j in range(n)]
        for i in range(1, n):
            temp = [float('inf')]*n
            for j in range(n):
                for k in range(-1, 2):
                    if j+k >=0 and j+k < n:
                        temp[j] = min(temp[j], dp[j+k])
            dp = [A[i][j] + temp[j] for j in range(n)]
        return min(dp)
```

## 129. Sum Root to Leaf Numbers
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.leaves = []
        self.dfs(root,'')
        
        return sum([int(i) for i in self.leaves])
        
    def dfs(self, root, path):
        '''
        Add the path from root to leaves as strings to the list 'leaves'
        '''
        if not root.left and not root.right:
            self.leaves.append(path+str(root.val))
            return
        
        if root.left:
            self.dfs(root.left, path+str(root.val))
        if root.right:
            self.dfs(root.right, path+str(root.val))
```

## 102. Binary Tree Level Order Traversal

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        cur_cnt, next_cnt, temp, queue, res = 1, 0, [], collections.deque(), []
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            temp.append(node.val)
            cur_cnt -= 1
            if node.left:
                queue.append(node.left)
                next_cnt += 1
            if node.right:
                queue.append(node.right)
                next_cnt += 1
            # if the current level runs out, reset
            if cur_cnt == 0:
                res.append(temp)
                temp, cur_cnt, next_cnt = [], next_cnt, 0
            
        return res
            
```
## 103. Binary Tree Zigzag Level Order Traversal
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        cur_cnt, next_cnt, temp, queue, res = 1, 0, [], [], []
        direction = 0 # indicates the direction on the current level. 0 == L to R
        queue.append(root)
        
        while queue:
            
            node = queue.pop(cur_cnt-1)
            temp.append(node.val)
            cur_cnt -= 1 
            # when we are moving from L to R, we append from L to R
            if direction == 0:
                if node.left:
                    queue.append(node.left)
                    next_cnt += 1
                if node.right:
                    queue.append(node.right)
                    next_cnt += 1
            else: # if we are moving from R to L, we append from R to L
                if node.right:
                    queue.append(node.right)
                    next_cnt += 1
                if node.left:
                    queue.append(node.left)
                    next_cnt += 1
            # if the current level runs out, reset and change direction
            if cur_cnt == 0:
                res.append(temp)
                temp, cur_cnt, next_cnt = [], next_cnt, 0
                direction = (direction+1)%2
            
        return res
```
## 144. Binary Tree Preorder Traversal

Iterative method:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        if root:
            stack.append(root)
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
```
## 145. Binary Tree Postorder Traversal
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        p = root
        while stack or p:
            if p:
                stack.append(p)
                res = [p.val]+res
                p = p.right
            else:
                node = stack.pop()
                p = node.left
        return res
```
## 91. Decode Ways
```

class Solution:
    def numDecodings(self, s: str) -> int:
        self.res = 0
        self.helper(s, '0', 0, 1)
        return self.res
    
    def helper(self, s, prefix, temp1, temp2):
        if not s:
            self.res += temp2
            return
        
        if int(prefix + s[0]) == 0:
            self.res = 0
            return 
        else:
            if prefix == '0':
                self.helper(s[1:], s[0], temp2, temp2)
            elif s[0] == '0' and int(prefix+s[0]) <= 26:
                self.helper(s[1:], s[0], temp1, temp1)
            elif s[0] == '0' and int(prefix+s[0]) > 26:
                self.res = 0
                return
            elif int(prefix+s[0]) > 26:
                self.helper(s[1:], s[0], temp2, temp2)
            else:
                self.helper(s[1:], s[0], temp2, temp1+temp2)                             
```


## 215. Kth Largest Element in an Array

Many different solutions:

```
# O(nlgn) time
def findKthLargest1(self, nums, k):
    return sorted(nums, reverse=True)[k-1]
    
# O(nk) time, bubble sort idea, TLE
def findKthLargest2(self, nums, k):
    for i in xrange(k):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                # exchange elements, time consuming
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[len(nums)-k]
    
# O(nk) time, selection sort idea
def findKthLargest3(self, nums, k):
    for i in range(len(nums), len(nums)-k, -1):
        tmp = 0
        for j in xrange(i):
            if nums[j] > nums[tmp]:
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return nums[len(nums)-k]
    
# O(k+(n-k)lgk) time, min-heap
def findKthLargest4(self, nums, k):
    # minheap
    array = nums[:k]
    heapq.heapify(array) # O(k)
    for num in nums[k:]: # O(n-k)
        if num > array[0]:
            heapq.heapreplace(array, num) # O(log k)
    return array[0]

    
# O(n) time, quick selection
def findKthLargest(self, nums, k):
    # convert the kth largest to smallest
    return self.findKthSmallest(nums, len(nums)+1-k)
    
def findKthSmallest(self, nums, k):
    if nums:
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]
 
# choose the right-most element as pivot   
def partition(self, nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low
```

## 216. Combination Sum III

```
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        if n >= 0 and n<= 50:
            self.dfs(k, n, [], 1)
        return self.res
        
    def dfs(self, k, target, path, start):
        if k == 0 and target == 0:
            self.res.append(path)
            return 
        elif start > target or start > 9:
            return 
        
        for x in range(start, 10):
            if x <= target:
                self.dfs(k-1, target-x, path+[x], x+1)
```
## 230. Kth Smallest Element in a BST

Use the iterative in-place traversal for BST and record how many nodes have been popped.
```
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack, node, cnt = [], root, 0
        while True:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            cnt += 1
            if cnt == k:
                return node.val
            node = node.right
```

## 226. Invert Binary Tree
```
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
```

## 92. Reverse Linked List II
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # mid_head is the m-th node in the original list
        if m == 1:
            mid_head = head
        
        else:
            i, prev, cur = 2, head, head.next
            while i < m:
                i, prev, cur = i+1, cur, cur.next 
            mid_head = cur 
        
        # reverse 
        cnt, slow, fast = 0, mid_head, mid_head.next
        while cnt < n-m:
            temp = fast.next
            fast.next, slow, fast = slow, fast, temp
            cnt += 1
        
        # attach the reversed part with the last part
        mid_head.next = fast
        # attach the first part (if m>1) with the reversed part
        if m > 1:
            prev.next = slow
        # if m == 1, we have to reset the head
        else:
            head = slow
        return head
```
## 492. Construct the Rectangle

```
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        start = math.floor(math.sqrt(area))
        for W in range(start, 0, -1):
            if area % W == 0:
                return [ area//W, W]
```

## 406. Queue Reconstruction by Height

The neat solution: 
```
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
```

My clumsy solution:
```
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        
        self.res = []
        
        min, loc = float('inf'), 0
        for i in range(len(people)):
            if people[i][1] == 0 and people[i][0] < min:
                min, loc = people[i][0], i
        self.res.append(people.pop(loc))
        aux = [x+[0] for x in people]
        for i in range(len(people)):
            self.findNext(aux, self.res[-1][0])
        
        return self.res
           
    def findNext(self, aux, prev):
        minH, loc =  float('inf'), 0
        for i in range(len(aux)):
            if aux[i][0] <= prev:
                aux[i][1], aux[i][2] = aux[i][1]-1, aux[i][2] + 1
            if aux[i][1] == 0 and aux[i][0] < minH:
                minH, loc = aux[i][0], i
            
        temp = aux.pop(loc)
        temp[1] += temp[2]
        self.res.append(temp[:2])
```
## 451. Sort Characters By Frequency

```
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        d, res = Counter(s), ''
        for key, val in sorted(d.items(), key = lambda x: x[1], reverse = True):
            res += key*val
        return res
```
## 445. Add Two Numbers II

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1, x2 = 0, 0
        while l1:
            x1 = x1*10+l1.val
            l1 = l1.next
        while l2:
            x2 = x2*10+l2.val
            l2 = l2.next
        x = x1 + x2
        
        head = ListNode(0)
        if x == 0: return head
        while x:
            v, x = x%10, x//10
            head.next, head.next.next = ListNode(v), head.next
            
        return head.next
```
## 403. Frog Jump

```
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        # steps[i] records the distances (if any) the frog jumped from the previous           # stone to reach ith stone
        steps = [[] for _ in range(len(stones))]
        steps[0] = [0]
        for i in range(len(stones)-1):
            if not steps[i]:
                continue
                
            M = max(steps[i])+1
            for j in range(i+1, len(stones)):
                dist_ij = stones[j]-stones[i]
                if dist_ij > M:
                    break
                elif dist_ij-1 in steps[i] or dist_ij in steps[i] or dist_ij+1 in steps[i]:
                    steps[j].append(dist_ij)
        
        return len(steps[-1]) > 0 
```

## 429. N-ary Tree Level Order Traversal

```
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res, cur, nxt, q = [[]], 1,0, collections.deque()
        q.append(root)
        while q:
            node, cur = q.popleft(), cur-1
            res[-1].append(node.val)
            q.extend(node.children)
            nxt += len(node.children)
            if cur == 0 and nxt > 0:
                res.append([])
                cur, nxt = nxt, 0
        return res
```
## 442. Find All Duplicates in an Array

Using `collections.Counter`:
```
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        d, res = Counter(nums), []
        for key in d:
            if d[key] == 2:
                res.append(key)
        return res
```

O(n) time, O(1) space solution:
```
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res
```

## 482. License Key Formatting

```
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-','').upper()
        l, res = len(S), ''
        q, r = l//K, l%K
        res = S[:r]
        for i in range(q):
            res += '-'+S[r+i*K: r+(i+1)*K]
        if r == 0:
            res = res[1:]
        return res
```
## 427. Construct Quad Tree
```
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid: return None
        
        if self.isLeaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        else:
            n = len(grid)
            return Node('*', False, \
                       self.construct([row[:n//2] for row in grid[:n//2]]), \
                       self.construct([row[n//2:] for row in grid[:n//2]]), \
                       self.construct([row[:n//2] for row in grid[n//2:]]), \
                       self.construct([row[n//2:] for row in grid[n//2:]]))
        
    def isLeaf(self, grid):
        return all ([grid[i][j]==grid[0][0] for i in range(len(grid)) for j in range(len(grid))])
```

## 459. Repeated Substring Pattern

```
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(1,l//2+1):
            q, r = l//i, l%i
            if r==0 and s[0]==s[i] and s[i-1]==s[-1]:
                sub, j = s[:i], 1
                while j < q:
                    if sub != s[j*i:j*i+i]: break
                    j += 1
                if j==q: return True
            else:
                continue
        return False
```
## 289. Game of Life

Direct method, use an extra matrix of the same size.
```
class Solution:
    def gameOfLife(self, board):
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 or board[i][j] == 2:
                    if self.nnb(board,i,j) == 3:
                        board[i][j] = 2
                else:
                    if self.nnb(board,i,j) < 2 or self.nnb(board,i,j) >3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0

    def nnb(self, board, i, j):
        m,n = len(board), len(board[0])
        count = 0
        if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]%2
        if i-1 >= 0:                count += board[i-1][j]%2
        if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]%2
        if j-1 >= 0:                count += board[i][j-1]%2
        if j+1 < n:                 count += board[i][j+1]%2
        if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]%2
        if i+1 < m:                 count += board[i+1][j]%2
        if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2
        return count
```

In-place method. The trick is to use the following representations:
0,2 are "dead", and "dead->live"
1,3 are "live", and "live->dead"
```
def gameOfLife(self, board):
    m,n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0 or board[i][j] == 2:
                if self.nnb(board,i,j) == 3:
                    board[i][j] = 2
            else:
                if self.nnb(board,i,j) < 2 or self.nnb(board,i,j) >3:
                    board[i][j] = 3
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2: board[i][j] = 1
            if board[i][j] == 3: board[i][j] = 0
            
def nnb(self, board, i, j):
    m,n = len(board), len(board[0])
    count = 0
    if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]%2
    if i-1 >= 0:                count += board[i-1][j]%2
    if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]%2
    if j-1 >= 0:                count += board[i][j-1]%2
    if j+1 < n:                 count += board[i][j+1]%2
    if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]%2
    if i+1 < m:                 count += board[i+1][j]%2
    if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2
    return count
```
## 238. Product of Array Except Self

Use extra space O(n):
```
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left[i], right[i] represent the products of the numbers on the left and right of nums[i], exclusive
        left, right = [1]*len(nums), [1]*len(nums)
        
        for i in range(1,len(nums)):
            left[i], right[-1-i] = left[i-1]*nums[i-1], right[-i]*nums[-i]
        
        return [left[i]*right[i] for i in range(len(nums))]
```

Same idea as above, with a clever manipulation to avoid extra space.
```
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
```
## 137. Single Number II
Using a counter:
```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            d[x] = d.get(x, 0)+1
        for x in d:
            if d[x] == 1:
                return x
```

## 260. Single Number III
```
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d, res = {}, []
        for x in nums:
            d[x] = d.get(x, 0)+1
        for x in d:
            if d[x] == 1:
                res.append(x)
        return res
```


Now use bitwise operations:
```
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x
        
        mask = 1
        while not(xor & mask):
            mask = mask << 1
        
        a, b = 0, 0
        for x in nums:
            if x & mask > 0:
                a ^= x
            else:
                b ^= x
        
        return [a,b]
```

## 264. Ugly Number II

```
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2,i3,i5 = 0 ,0, 0
        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3]*3, ugly[i5]*5
            m = min(u2,u3,u5)
            ugly.append(m)
            if m == u2:
                i2 += 1
            if m == u3:
                i3 += 1
            if m == u5:
                i5 += 1
            n -= 1
        return ugly[-1]
```

## 105. Construct Binary Tree from Preorder and Inorder Traversal
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        head_val = preorder.pop(0)
        root, ind = TreeNode(head_val), inorder.index(head_val)
        left_child = self.buildTree(preorder[:ind], inorder[:ind])
        right_child = self.buildTree(preorder[ind:], inorder[ind+1:])
        root.left, root.right = left_child, right_child
        return root
```
## 106. Construct Binary Tree from Inorder and Postorder Traversal

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        head_val = postorder[-1]
        root, ind, l = TreeNode(head_val), inorder.index(head_val), len(inorder)
        left_child = self.buildTree(inorder[:ind], postorder[:ind])
        right_child = self.buildTree(inorder[ind+1:], postorder[ind:l-1])
        root.left, root.right = left_child, right_child
        return root
```
## 109. Convert Sorted List to Binary Search Tree

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.construct(nums)
            
    def construct(self, nums):
        if not nums:
            return None
        n = len(nums)//2
        head = TreeNode(nums[n])
        head.left = self.construct(nums[:n])
        head.right = self.construct(nums[n+1:])
        return head
```

## 114. Flatten Binary Tree to Linked List
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        left, right = root.left, root.right
        self.flatten(right)
        if left:
            self.flatten(left)
            root.left, root.right = None, left
            bottom = left
            while bottom.right:
                bottom = bottom.right
            bottom.right = right
```
## 116. Populating Next Right Pointers in Each Node

```
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        
        root.left.next = root.right
        l, r = root.left, root.right
        while l.right:
            l.right.next = r.left
            l, r = l.right, r.left
        self.connect(root.left)
        self.connect(root.right)
        return root
```

## 117. Populating Next Right Pointers in Each Node II

The idea is view each level as a singly linked list. We need to use the nodes from the previous level to traverse, where `head` and `tail` are used to keep track of the starting of the previous level.

```
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = tail = Node(0)
        node = root
        while node:
            for x in (node.left, node.right):
                tail.next = x
                if x:
                    tail = x
            if node.next:
                node = node.next
            else:
                node, tail = head.next, head
        return root
```

## 173. Binary Search Tree Iterator
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ind = 0
        self.list = []
        self.inplace(root)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.list[self.ind]
        self.ind += 1
        return res
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.ind < len(self.list)
    
    def inplace(self, root):
        if not root:
            return 
        self.inplace(root.left)
        self.list.append(root.val)
        self.inplace(root.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
## 128. Longest Consecutive Sequence
```
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, d = 0 , {}
        for x in nums:
            d[x] = d.get(x, 1)
        
        for k in d:
            if d[k] == 1:
                cnt, down, up = 1,  k-1 , k+1
                d[k] = 0
                while up in d and d[up]==1:
                    d[up] = 0
                    cnt, up = cnt + 1, up + 1
                while down in d and d[down]==1:
                    d[down] = 0
                    cnt, down = cnt + 1, down - 1
                res = max(res, cnt)
        return res
```
## 199. Binary Tree Right Side View

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, q, cur, nxt = [], collections.deque(), 1, 0
        q.append(root)
        while q:
            node, cur = q.popleft(), cur - 1
            if node.left:
                q.append(node.left)
                nxt += 1
            if node.right:
                q.append(node.right)
                nxt += 1
            if cur == 0:
                res.append(node.val)
                cur, nxt = nxt, 0
        return res
```

## 131. Palindrome Partitioning
```
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(1, len(s)):
            if self.isPalindrome(s[:i]):
                res += [[s[:i]]+x for x in self.partition(s[i:])]
        return res+[[s]] if self.isPalindrome(s) else res
        
    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            else:
                left, right = left+1, right-1
        return True
```
## 41. First Missing Positive
```
 def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n
```
## 162. Find Peak Element

A binary search problem in disguise! The trick is that if `nums[left-1]< nums[left]` and `nums[right]>nums[right+1]` and also adjacent elements are different, then by the picture, there must be a local max somewhere in between `left` and `right`.

```
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right-1:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left if nums[left]>=nums[right] else right
```
## 200. Number of Islands

Go through the entire grid. Whenever we encounter a `'1'`, we use a DFS function to explore the entire island and change the visited island areas inplace.

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.explore(grid, m, n, i, j)
        return res 
    
    def explore(self, grid, m, n, x, y):
        grid[x][y] = 3
        stack = [(x,y)]
        while stack:
            (i, j) = stack.pop()
            if i-1 >= 0 and grid[i-1][j]=='1':
                grid[i-1][j] = 3
                stack.append((i-1,j))
            if i+1 < m and grid[i+1][j]=='1':
                grid[i+1][j] = 3
                stack.append((i+1,j))
            if j-1 >= 0 and grid[i][j-1]=='1':
                grid[i][j-1] = 3
                stack.append((i,j-1))
            if j+1 < n and grid[i][j+1]=='1':
                grid[i][j+1] = 3
                stack.append((i,j+1))
```
## 142. Linked List Cycle II

See [link](https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation) for a detailed explanation (tho note that it contains some minor mistakes in his explanation)

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head
```

## 299. Bulls and Cows
```
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d1, d2, A, B = {},{},0,0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                A += 1
            else:
                d1[secret[i]] = d1.get(secret[i], 0) + 1
                d2[guess[i]] = d2.get(guess[i], 0) + 1
        for x in d1:
            if x in d2:
                B += min(d1[x], d2[x])
        
        return str(A)+'A'+str(B)+'B'
```
## 201. Bitwise AND of Numbers Range

```
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        b1, b2 = format(m, 'b'), format(n, 'b')
        b1 = '0'*(len(b2)-len(b1)) + b1
        k = len(b1)
        
        for i in range(len(b1)):
            if b1[i] != b2[i]:
                k = i
                break
        return int(b1[:k]+'0'*(len(b1)-k), 2)
```
## 221. Maximal Square



```
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m , n = len(matrix), len(matrix[0])
        
        # dp[i][j] stands for the maximal size of squares whose bottom-right corner is at (i,j) 
        
        dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]
       
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
               
        return max([max(row) for row in dp]) ** 2
```
## 98. Validate Binary Search Tree

```
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -float('inf'), float('inf'))
    
    def helper(self, node, lower_bound, upper_bound):
        if not node: return True
        if node.val >= upper_bound or node.val <= lower_bound:
            return False
        left = self.helper(node.left, lower_bound, node.val)
        right = self.helper(node.right, node.val, upper_bound)
        return left and right
```
## 495. Teemo Attacking

```
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        res, n = duration, len(timeSeries)
        for i in range(n-1):
            res += min(duration, timeSeries[i+1]-timeSeries[i])
        return res
```
## 454. 4Sum II

```
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = collections.Counter(a+b for a in A for b in B)
       
        return sum(AB[-c-d] for c in C for d in D)
```

A basic way of realizing the above algorithm:
```
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        res, i1 = 0, 0
        while i1 < len(A):
            i2, mult1 = 0, 1
            while i1+1 < len(A) and A[i1+1] == A[i1]:
                mult1 += 1
                i1 += 1
            while i2 < len(B):
                twosum, mult2 = A[i1]+B[i2], 1
                while i2+1 < len(B) and B[i2+1] == B[i2]:
                    mult2 += 1
                    i2 += 1
                
                i3 = 0
                while i3 < len(C):
                    wanted, mult3 = -C[i3]-twosum, 1
                    while i3+1<len(C) and C[i3+1] == C[i3]:
                        mult3 += 1
                        i3 += 1
                    temp, i4 = 0, 0
                    while i4 < len(D):
                        
                        if D[i4] > wanted:
                            break
                        if D[i4] == wanted:
                            temp += 1
                            i4 += 1
                        elif D[i4] < wanted:
                            i4 += 1
                    res += temp*mult1*mult2*mult3
                    i3 += 1
                i2 += 1
            i1 += 1
        return res
```

## 419. Battleships in a Board

```
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        res, m, n = 0, len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if (i-1 < 0 or (i-1 >= 0 and board[i-1][j] == '.')) and (j-1<0 or (j-1>=0 and board[i][j-1]  == '.')):
                        res += 1
        return res
```

## 922. Sort Array By Parity II

This is a in-place method.
```
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        cur_odd, cur_even= 0, 0
        for i in range(len(A)):
            if A[i]%2 == 1:
                cur_odd += 1
                if cur_even > cur_odd:
                    A[2*cur_odd-1], A[i] =  A[i], A[2*cur_odd-1] 
            else:
                cur_even += 1
                if cur_odd >= cur_even:
                    A[2*cur_even-2], A[i] = A[i], A[2*cur_even-2]
        return A
```
## 942. DI String Match
```
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        min, max, res =0, len(S), [0]*(len(S)+1)
        for i in range(len(S)):
            if S[i] == 'I':
                res[i], min = min, min+1
            else:
                res[i], max = max, max-1
        res[-1] = min
        
        return res
```
## 284. Peeking Iterator
```
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.items = []
        self.ind = 0
        while iterator.hasNext():
            self.items.append(iterator.next())
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.items[self.ind]
        

    def next(self):
        """
        :rtype: int
        """
        temp, self.ind = self.items[self.ind], self.ind+1
        return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ind < len(self.items)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```

## 209. Minimum Size Subarray Sum
```
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total, left, res = 0, 0, len(nums)+1
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1
        return res if res < len(nums)+1 else 0
```
## 211. Add and Search Word - Data structure design

```
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {0:''}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words[len(word)] = self.words.get(len(word), [])+[word]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) not in self.words:
            return False
        
        for w in self.words[len(word)]:
            match = True
            for i in range(len(word)):
                if word[i] == '.':
                    continue
                else:
                    if word[i] != w[i]:
                        match = False
                        break
            if match == True: return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
## 222. Count Complete Tree Nodes

Compare the depth between left sub tree and right sub tree.
- If it is equal, it means the left sub tree is a full binary tree
- If it is not , it means the right sub tree is a full binary tree

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        if leftDepth == rightDepth:
            return 2**leftDepth + self.countNodes(root.right)
        else:
            return 2**rightDepth + self.countNodes(root.left)
        
    def depth(self, root):
        if not root:
            return 0
        return 1+self.depth(root.left)
```
## 227. Basic Calculator II
```
class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(' ', '')
        stack, num, op = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit(): num = num * 10 + int(s[i])
            if not s[i].isdigit() or i==len(s)-1:
                if op == '+': stack.append(num)
                elif op == '-': stack.append(-num)
                elif op == '*': stack.append(stack.pop()*num)
                else:
                    temp = stack.pop()
                    if temp < 0 and temp%num != 0:
                        stack.append(temp//num + 1)
                    else:
                        stack.append(temp//num)
                num, op = 0, s[i]
        return sum(stack)
```
## 241. Different Ways to Add Parentheses
```
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in '+-*':
                sign = input[i]
                res += [self.helper(n1,n2,sign) for n1 in self.diffWaysToCompute(input[:i]) for n2 in self.diffWaysToCompute(input[i+1:])]
        return res
                
        
    def helper(self, n1, n2, sign):
        if sign == '+':
            return n1+n2
        if sign == '-':
            return n1 - n2
        if sign == '*':
            return n1 * n2
```
## 220. Contains Duplicate III

Bucket sort (or pigeon-hole principle).

```
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t<0 or k==0: return False
        d, s = {}, t+1
        for i in range(len(nums)):
            m = nums[i]//s
            if m in d:
                return True
            if m-1 in d and nums[i]-d[m-1] <= t:
                return True
            if m+1 in d and d[m+1]-nums[i] <= t:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i-k]//s]
        return False
```
## 279. Perfect Squares
```
class Solution:
    def numSquares(self, n: int) -> int:
        lst = [i**2 for i in range(1, int(n**0.5)+1)]
        res, toCheck = 0, {n}
        while toCheck:
            res += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x==y: return res
                    if x < y: break
                    temp.add(x-y)
            toCheck = temp
        return res
```
## 754. Reach a Number
```
class Solution:
    def reachNumber(self, target: int) -> int:
        # Equivalent to find the smallest positive integer i such that:
        # 1. 1+2+...+i >= target;
        # 2. 1+2+...+i and target share the same parity.

        target = abs(target)
        i = int(target**0.5)
        temp = i*(i+1)/2
        while  temp < target or (target-temp)%2:
            i += 1
            temp = i*(i+1)/2
        return i
```
## 334. Increasing Triplet Subsequence
```
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # We just need to find a way to track the most promising increasing 
        # subsequence of length 2 (i.e. whose elements are smallest so far)
        track = [float('inf')]*2
        for i in range(len(nums)):
            if nums[i] > track[1]:
                return True
            if nums[i] < track[0]:
                track[0] = nums[i]
            elif track[0] < nums[i] < track[1]:
                track[1] = nums[i]
        return False
```
## 300. Longest Increasing Subsequence
```
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        track = [nums[0]]
        for i in range(1,len(nums)):
            temp = nums[i]
            if temp > track[-1]:
                track.append(temp)
            else:
                for j in range(len(track)):
                    if temp <= track[j]:
                        track[j] = temp
                        break
        return len(track)
```
## 646. Maximum Length of Pair Chain
```
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return 0
    
        pairs = sorted(pairs, key = lambda x: (x[0], x[1]))
        track = [pairs[0]]
        for i in range(1, len(pairs)):
            temp = pairs[i]
            for j in range(len(track)):
                if temp[0] > track[-1][1]:
                    track.append(temp)
                elif j==0 and temp[1] <= track[j][1]:
                    track[j] = temp
                    break
                elif j-1 >= 0 and temp[0] > track[j-1][1] and temp[1] <= track[j][1]:
                    track[j] = temp
                    break
        return len(track)
```
## 491. Increasing Subsequences
The trick is to use tuples instead of lists since lists are not hashable (hence we cannot easily get rid of the repetitive lists).
```
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = {()}
        for n in nums:
            res = res.union({s+(n,) for s in res if not s or s[-1]<=n})
        return [s for s in res if len(s)>1]
```
## 398. Random Pick Index

```
class Solution:

    def __init__(self, nums: List[int]):
        self.dic = {}
        for i, n in enumerate(nums):
            self.dic[n] = self.dic.get(n, [])+[i]

    def pick(self, target: int) -> int:
        return random.choice(self.dic[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```
## 357. Count Numbers with Unique Digits
```
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        # dp[i] is the total number of integer numbers with i distinct digits.
        dp = [0]*11
        dp[1] = 10
        dp[2] = 81
        for i in range(3, min(11,n+1)):
            dp[i] = dp[i-1] *(11-i)
        
        return sum(dp[:n+1])
```
## 313. Super Ugly Number

```
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly= [1]
        idx, candidates = [0]*len(primes), [x for x in primes]
        while n > 1:
            m = min(candidates)
            i = candidates.index(m)
            idx[i] += 1
            if m > ugly[-1]:
                ugly.append(m)
                n -= 1
            candidates[i] = ugly[idx[i]] * primes[i]
            
        return ugly[-1]
```
## 309. Best Time to Buy and Sell Stock with Cooldown

A good example of DP with more than one states to handle.

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        buy, sell = [0] * (len(prices)+2), [0] * (len(prices)+2)
        buy[1] = -prices[0]
        for i in range(2, len(buy)):
            buy[i] = max(sell[i-2]-prices[i-2], buy[i-1])
            sell[i] = max(buy[i-1]+prices[i-2], sell[i-1])
        return sell[-1]
```

## 310. Minimum Height Trees

Method 1: Remove leaves until we have at most two leaves left. Those two nodes is the mid points of the longest path in the tree, which are the roots of the minimal depth rooted trees.
```
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        adjacent = collections.defaultdict(set)
        for i, j in edges:
            adjacent[i].add(j)
            adjacent[j].add(i)
        
        leaves = [i for i in adjacent if len(adjacent[i])==1]
        
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for i in leaves:
                j = adjacent[i].pop()
                adjacent[j].remove(i)
                if len(adjacent[j]) == 1: newleaves.append(j)
            leaves = newleaves
        return leaves
```
## 301. Remove Invalid Parentheses

```
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            valid = [x for x in level if isvalid(x)]
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s)) if s[i] in '()'}
```

## 318. Maximum Product of Word Lengths
```
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # The essential part is to find a one to quickly check, store and 
        # access the alphabet for each word. We use bitwise operations to store those.
        
        
        d = {}
        for w in words:
            alphabet = 0
            for s in set(w):
                alphabet |= (1 << (ord(s)-ord('a')))
            
            d[alphabet] = max(d.get(alphabet, 0), len(w))
        
        return max([d[x]*d[y] for x in d for y in d if not x&y]+[0])
```


## 589. N-ary Tree Preorder Traversal
```
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node.children:
                stack += node.children[::-1] 
            res.append(node.val)
        return res
```

## 590. N-ary Tree Postorder Traversal
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack += node.children
        return res[::-1]
```
## 494. Target Sum

Brute-force:

```
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            if S == 0: return 1
            else: return 0
        return self.findTargetSumWays(nums[1:], S-nums[0])+self.findTargetSumWays(nums[1:], S+nums[0])
```


DP:
```
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # Idea: from left to right, we add nums[i] into
        # consideration. Each time, we use a dictionary to record 
        # the possible outcome (key) and how many ways to come up with 
        # each outcome (value) using the first several numbers.
        
        if not nums: return 0
        if nums[0] == 0:
            dic = {0:2}
        else: dic = {nums[0]:1, -nums[0]:1}
        
        for x in nums[1:]:
            temp = {}
            for d in dic:
                temp[d+x] = temp.get(d+x, 0) + dic[d]
                temp[d-x] = temp.get(d-x, 0) + dic[d]
            dic = temp
        return dic.get(S, 0)
```

## 413. Arithmetic Slices
```
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3: return 0
        # compute the differences between adjacent numbers
        diff = [A[i]-A[i-1] for i in range(1, len(A))]
        i, lengths = 0, []

        # go through the list of differences to find the lengths of the maximal contigent arithmetic sublists
        # Here our 'l' is actually length-1
        while i<len(diff):
            l = 1
            while i+1<len(diff) and diff[i+1]==diff[i]:
                i, l = i+1, l+1
            if l > 1:
                lengths.append(l)
            i += 1
        
        return sum([l*(l-1)//2 for l in lengths])
```
## 486. Predict the Winner
```
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp[start][end] = max total for the first player using nums[start:end+1], assuming both played optimally.
        # dp[i][j] = max(sum(nums[i:j+1])-dp[i+1][j], sum(nums[i:j+1])-dp[i][j-1])

        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        left_sums = [0]*n
        left_sums[0] = nums[0]
        for i in range(1,n):
            left_sums[i] = nums[i]+left_sums[i-1]
        for j in range(n):
            for i in range(j, -1, -1):
                if i==j:
                    dp[i][j] = nums[i]
                else:
                    if i > 0:
                        total = left_sums[j]-left_sums[i-1]
                    else: total = left_sums[j]
                    dp[i][j] = max(total-dp[i+1][j], total-dp[i][j-1])
        return dp[0][n-1]*2 >= left_sums[-1]
```


## 498. Diagonal Traverse

```
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        
        res = []
        m, n, up = len(matrix), len(matrix[0]), 1
        i, j = 0, 0
        while i < m-1 or j < n-1:
            
            if up:
                while i-1>=0 and j+1 < n:
                    res.append(matrix[i][j])
                    (i, j) = (i-1,j+1)
                    
                res.append(matrix[i][j])
                if i == 0 and j+1 < n:
                    j = j+1
                else:
                    i = i+1
                up = 0
            else:
                while i+1 < m and j-1>=0:
                    res.append(matrix[i][j])
                    (i,j) = (i+1, j-1)
                    
                res.append(matrix[i][j])
                if j == 0 and i+1 < m:
                    i = i+1
                else:
                    j = j+1
                up = 1
        res.append(matrix[i][j])
        return res
```

## 481. Magical String
```
class Solution:
    def magicalString(self, n: int) -> int:
        S = [1,2,2]
        idx = 2
        while len(S) < n:
            S += [3-S[-1]]*S[idx]
            idx += 1
        return S[:n].count(1)
```

## 462. Minimum Moves to Equal Array Elements II
```
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if  len(nums) < 2: return 0
        
        nums.sort()
        n = len(nums)
        return min(sum([abs(x-nums[n//2]) for x in nums]), sum([abs(x-nums[n//2-1]) for x in nums]))
```

##  416. Partition Equal Subset Sum
```
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum%2 == 1: return False
        
        target = Sum/2
        obtainable = {0}
        for n in nums:
            if target in obtainable:
                return True
            obtainable |= {n+x for x in obtainable}
        return False
```
## 470. Implement Rand10() Using Rand7()
```
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        i = rand7()
        while i == 7:
            i = rand7()
        x = i%2
        y = rand7()
        while y > 5:
            y = rand7()
        return x*5+y
 ```

## 452. Minimum Number of Arrows to Burst Balloons
 ```
 class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        res, i = 0, 0
        while i < len(points):
            res, right_bd = res + 1, points[i][1]
            while i+1<len(points) and points[i+1][0] <= right_bd:
                right_bd = min(right_bd, points[i+1][1])
                i += 1
            i += 1
        return res
```
## 450. Delete Node in a BST
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return 
        
        sentinel = TreeNode(float('inf'))
        sentinel.left = root
        
        pre, cur = sentinel, root
        while cur and cur.val != key:
            if cur.val > key:
                pre, cur = cur, cur.left
            else:
                pre, cur = cur, cur.right
        if not cur: return root
        
        if cur.right: # use the minimal node from right to replace
            (cur.val, cur.right) = self.removeMin(cur.right)
        elif cur.left and not cur.right: # use the max node from left to replace
            (cur.val, cur.left) = self.removeMax(cur.left)
        else:
            if pre.val > key:
                pre.left = None
            else:
                pre.right = None
        return sentinel.left
    
    def removeMin(self, root):
        # we assume tree is not empty
        if not root.left: return (root.val, root.right)
        else:
            pre, cur = root, root.left
            while cur.left:
                pre, cur = cur, cur.left
            Min = cur.val
            pre.left = cur.right
            return (Min, root)
        
    def removeMax(self, root):
        if not root.right: return (root.val, root.left)
        else:
            pre, cur = root, root.right
            while cur.right:
                pre, cur = cur, cur.right
            Max = cur.val
            pre.right = cur.left
            return (Max, root)
```
## 477. Total Hamming Distance
```
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums: return 0
        n, k = len(nums), len(bin(max(nums)))-2
        counts = [0] * k
        for num in nums:
            s = bin(num)[2:][::-1]
            for i in range(len(s)):
                if s[i] == '1':
                    counts[i] += 1
        return sum([x*(n-x) for x in counts])
```

## 784. Letter Case Permutation
```
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S: return []
        res = ['']
        for letter in S:
            if letter.isdigit():
                res = [x+letter for x in res]
            else:
                res = [x+l for x in res for l in [letter.lower(), letter.upper()]]
        return res
```

## 421. Maximum XOR of Two Numbers in an Array

Explanation link: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/171747/Python-O(n)-solution-easily-explained
General form of solution is to find two numbers which have the highest bits complementing each other (0 and 1). Then store that max, look at the next less significant bit and see if another two numbers complement each other (which includes the bits sets from the previous max). If so, this number will
be greater than the previous maximum. Steps:

Find the new possible maximum by setting the next bit to 1 on the current maximum
use a mask with all 1s up to the current bit i and & all numbers with this mask to see which bit in that number up to bit i are set as 1.
Critical part: to solve this in O(n) it's important to know that If a ^ b = c, then a ^ c = b and c ^ b = a. So, if we are looking for a particular number (in our case a possible maximum) we can do the following search: iterate in the numbers that we &'d with the mask. If our potental maximum is c, and our current number is a, we're looking for another number b that XOR'd with a gives c. Since we also know from above that a ^ c = b, we can just look for b it directly in our numbers (i.e. b = a ^ c, or in my code, bit ^ possible_mx).

```
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res, mask = 0, 0
        for i in range(31, -1 ,-1):
            temp_max, mask = res | 1<<i, mask | 1 << i
            bits = set()
            for n in nums:
                bits.add(n & mask)
            for bit in bits:
                if bit ^ temp_max in bits:
                    res = temp_max
                    break
        return res
```
## 458. Poor Pigs

[Explanation:](https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution)

```
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs, trial_num = 0, minutesToTest//minutesToDie+1
        while trial_num ** pigs < buckets:
            pigs += 1
        return pigs
```
## 464. Can I Win

Just a recursive brute-force with cache to save time.
```
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}

        def can_win(choices, remainder):
            # if the largest choice exceeds the remainder, then we can win!
            if choices[-1] >= remainder:
                return True

            # if we have seen this exact scenario play out, then we know the outcome
            seen_key = tuple(choices)+ (remainder,)
            if seen_key in seen:
                return seen[seen_key]

            # we haven't won yet.. it's the next player's turn.
            # importantly, if we win just one permutation then
            # we're still on our way to being able to 'force their hand'
            for index in range(len(choices)):
                if not can_win(choices[:index] + choices[index + 1:], remainder - choices[index]):
                    seen[seen_key] = True
                    return True

            # uh-oh if we got here then next player won all permutations, we can't force their hand
            # actually, they were able to force our hand :(
            seen[seen_key] = False
            return False


        # note: usefully, choices is already sorted
        choices = list(range(1, maxChoosableInteger + 1))

        # let's do some quick checks before we journey through the tree of permutations
        summed_choices = sum(choices)

        # if all the choices added up are less then the total, no-one can win
        if summed_choices < desiredTotal:
            return False

        # if the sum matches desiredTotal exactly, then as
        # long as there is an odd number of choices then first player wins
        if summed_choices == desiredTotal and len(choices) % 2:
            return True

        # slow: time to go through the tree of permutations
        return can_win(choices, desiredTotal)
```
## 86. Partition List
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Use two linked lists to store the nodes less than x and the nodes greater than or equal to x, respectively
        """
        if not head: return head
        
        sentinel1 = ListNode(1)
        sentinel2 = ListNode(2)
        node1, node2 = sentinel1, sentinel2
        cur, nxt = head, head.next
        
        while cur:
            nxt = cur.next
            if cur.val < x:
                node1.next = cur
                node1 = cur
            else:
                node2.next = cur
                node2 = cur
            cur.next = None
            cur = nxt
            
        if sentinel1.next:
            node1.next = sentinel2.next
            return sentinel1.next
        else:
            return sentinel2.next
```
## 127. Word Ladder

The most beautiful part of this answer lies in the construction of the function `construct_dict`, which gives a quick access of the fact whether two words are adjacent or not (i.e. can be changed from one to another by just changing a single letter).
```
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = collections.deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(set(wordList))
        return bfs_words(beginWord, endWord, d)
```
## 390. Elimination Game
```
class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.helper(n, True)
        
    def helper(self, n, L2R):
        if n==1: return 1
        # if from left to right, simply remove all the odd numbers
        if L2R:
            return 2*self.helper(n//2, False)
        # if from right to left and length is odd, again remove odd numbers
        elif n%2 == 1:
            return 2*self.helper(n//2, True)
        # if from right to left and length is even, remove even numbers
        else:
            return 2*self.helper(n//2, True)-1
```
## 611. Valid Triangle Number
```
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        nums.sort()
        for i in range(n-1, 1, -1):
            low, hi = 0, i-1
            while low < hi:
                if nums[low]+nums[hi] > nums[i]:
                    res += hi-low
                    hi -= 1
                else:
                    low += 1
        return res
```

## 228. Summary Ranges
```
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # use a dictionary to store the ranges. The key is the current right end point of the interval + 1 (end+1), and the key is the current left end pointof the interval (start).
        # This works for not sorted arrays as well.

        d, res = {}, []
        for n in nums:
            if n in d:
                start = d.pop(n)
                d[n+1] = start
            else:
                d[n+1] = n
        for key in d:
            if d[key] == key-1:
                res.append(str(key-1))
            else:
                res.append(str(d[key])+'->'+str(key-1))
        return res
```

## 93. Restore IP Addresses
```
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # A valid IP address consists of four numbers, each between 0 and 255 inclusive, separated by dot. 0 can only be the leading digit if the number is 0.
        # Typical DFS.
        self.res = []
        self.dfs(s, [])
        return ['.'.join(path) for path in self.res]
        
    def dfs(self, s, path):
        if len(s) > (4-len(path))*3:
            return 
        if not s and len(path) == 4:
            self.res.append(path)
            return
        for i in range(1, min(4, len(s)+1)):
            if 0 <= int(s[:i]) <= 255:
                self.dfs(s[i:], path+[str(s[:i])])
            else:
                break
            if (i == 1 and s[:i]=='0'):
                break
```
## 130. Surrounded Regions

```
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        
        m, n = len(board), len(board[0])
        self.record = [[0]*n for _ in range(m)]
        
        def dfs(board, i, j):
            self.record[i][j] = 1
            stack = [(i,j)]
            while stack:
                (x,y) = stack.pop()
                if x-1 >= 0 and board[x-1][y]=='O' and self.record[x-1][y] == 0: 
                    self.record[x-1][y] = 1
                    stack.append((x-1, y))
                if x+1 < m and board[x+1][y]=='O' and self.record[x+1][y] == 0: 
                    self.record[x+1][y] = 1
                    stack.append((x+1, y))
                if y-1 >= 0 and board[x][y-1]=='O' and self.record[x][y-1] == 0: 
                    self.record[x][y-1] = 1
                    stack.append((x, y-1))
                if y+1 < n and board[x][y+1]=='O' and self.record[x][y+1] == 0: 
                    self.record[x][y+1] = 1
                    stack.append((x, y+1))
            return 
    
        for i in [0,m-1]:
            for j in range(1, n-1):
                if board[i][j] == 'O' and not self.record[i][j]:
                    dfs(board, i,j)
        for j in [0,n-1]:
            for i in range(m):
                if board[i][j]=='O' and not self.record[i][j]:
                    dfs(board, i, j)
        for i in range(m):
            for j in range(n):
                if self.record[i][j]==0:
                    board[i][j] = 'X'
        return 
```
## 134. Gas Station

Here is a quick proof of the statement: if the total sum of `gas[i]-cost[i]` is nonnegative, then there exists a solution.

Suppose the sum of all terms of the form gas[i]-cost[i] is greater than or equal to 0. Choose an index i_0 such that starting from i_0 in the clockwise direction we obtain the largest possible partial sum of the form gas[i_0]-cost[i_0]+gas[i_0+1]-cost[i_0+1]+...+gas[i_1]-cost[i_1], among all possible choice of i_0 and i_1(here we are imagine the indices are all mode len(gas), thus a circle), denote this partial sum by S.

We claim that i_0 is a solution (we do not assume uniqueness of the solution).

Suppose it is not the case. Then either we can find an index i_2 between i_0 and i_1, or between i_1 and i_0 (remember, we are considering a circle, so the order matters!), such that the partial sum from i_0 to i_2 is less than 0, then one can easily construct a contradiction. If i_2 in between i_0 and i_1, we simply consider the partial sum from i_2+1 to i_1, which is S plus some positive number, contradicting that S is the largest partial sum. If i_2 lies in between i_1 and i_0, then, since the total sum is nonnegative, we know that the partial sum from i_2+1 to i_0 is strictly positive, thus, the partial sum from i_2+1 to i_1 is again strictly greater than S, again contradicts our assumption that S is maximal.
```
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res, net, total = 0, 0, 0
        for i in range(len(gas)):
            net += gas[i] - cost[i]
            if net < 0:
                total +=  net
                net = 0
                res = i+1
        total += net
        if total < 0: return -1
        
        return res
```

## 133. Clone Graph
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copied = {}
        res = Node(node.val,[])
        copied[node] = res
        stack=[node]
        while stack:
            origin = stack.pop()
            copy = copied[origin]
            for neighbor in origin.neighbors:
                if neighbor not in copied:
                    copy_neighbor = Node(neighbor.val,[])
                    copied[neighbor]=copy_neighbor
                    stack.append(neighbor)
                else:
                    copy_neighbor = copied[neighbor]
                copy.neighbors.append(copy_neighbor)
        return res
```
## 138. Copy List with Random Pointer

```
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur,dic = head, {}
        # copy nodes:
        while cur:
            dic[cur] = Node(cur.val, None, None)
            cur = cur.next
        # copy next and random attributes
        cur = head
        while cur:
            if cur.next:
                dic[cur].next = dic[cur.next]
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]
```

## 115. Distinct Subsequences

Brute-force recursive solution:

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.distinctCount(s, 0, t, 0)
    
    def distinctCount(self, s, pos1, target, pos2):
        '''
        Count the number of disctinct subsequences of s[pos1:] which equals target[pos2:].
        '''
        if len(target)-pos2 > len(s)-pos1:
            return 0
        if pos2 == len(target)-1:
            return s[pos1:].count(target[-1])
        
        res = 0
        for i in range(pos1, len(s)):
            if s[i] != target[pos2]: continue
            else:
                res += self.distinctCount(s, i+1, target, pos2+1)
        return res
```

Another solution using hash maps. Idea is that go through `s` to generate a dictionary whose keys are letters in `s` and the values are the positions of the letters. Then we just need to count how many strictly increasing sequences we can generate by `d[s[1]], d[s[2]],...,d[s[-1]]`.

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],[])+[i]
        for letter in set(t):
            if len(d.get(letter,[])) < t.count(letter):
                return 0
        return len(self.generateIncreasingTuples(d, t))
    def generateIncreasingTuples(self, d, t):
        res = [[-1]]
        for letter in t:
            res += [s+[x] for s in res for x in d[letter] if s[-1] < x]
        return [x for x in res if len(x) == len(t)+1]
```

Turns out it is another DP problem:

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sl, tl = len(s), len(t)
        if tl > sl: return 0
        
        # dp[i][j] equals the number of matches between s[:i] and t[:j]
        dp = [[0]*(tl+1) for _ in range(sl+1)]
        # if j==0, t[:0] is empty string, automatically matches with all
        for i in range(sl+1):
            dp[i][0] = 1
        for j in range(1, tl+1):
            for i in range(1,sl+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
```
## 164. Maximum Gap
```
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2: return 0
        
        nums = self.radixSort(nums)
        return max(nums[i+1]-nums[i] for i in range(len(nums)-1))
        
    def radixSort(self, nums):
        k = len(bin(max(nums)))-2
        for i in range(k):
            mask = 1 << i
            zeros, ones = [], []
            for n in nums:
                if n & mask:
                    ones.append(n)
                else:
                    zeros.append(n)
            nums = zeros + ones
        return nums
```
## 223. Rectangle Area
```
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (C-A)*(D-B)+(G-E)*(H-F)-self.overlapArea(A,B,C,D,E,F,G,H)
    
    def overlapArea(self, A, B, C,D,E,F,G,H):
        if A <= E <= C:
            left, right = E, min(C, G)
        elif E <= A <= G:
            left, right = A, min(C,G)
        else:
            return 0
        
        if B <= F <= D:
            low, high = F, min(H, D)
        elif F <= B <= H:
            low, high = B, min(H, D)
        else:
            return 0
        return (right-left)*(high-low)
```
## 229. Majority Element II
Boyer-Moore Majority Vote algorithm: see [link](http://goo.gl/64Nams)
Can be easily generalized to work for any number of majority vote.
```
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        cand1, cand2, cnt1, cnt2 = 0,1,0,0
        for n in nums:
            if n==cand1: cnt1 += 1
            elif n==cand2: cnt2 += 1
            elif cnt1==0: cand1, cnt1 = n, 1
            elif cnt2==0: cand2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [x for x in (cand1,cand2) if nums.count(x) > len(nums)//3]
```
## 304. Range Sum Query 2D - Immutable

Perfect example of trade off between space and time.
```
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = matrix
        if matrix and matrix[0]:
            # self.sums record the sums from (0,0) to (i,j)
            for i in range(1,len(matrix)):
                self.sums[i][0] += self.sums[i-1][0]
            for j in range(1, len(matrix[0])):
                self.sums[0][j] += self.sums[0][j-1]
            for i in range(1,len(matrix)):
                for j in range(1,len(matrix[0])):
                    self.sums[i][j] = self.sums[i][j]+self.sums[i-1][j]+self.sums[i][j-1]-self.sums[i-1][j-1]

                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if (row1,col1)==(0,0): return self.sums[row2][col2]
        elif row1==0:
            return self.sums[row2][col2] - self.sums[row2][col1-1]
        elif col1 == 0:
            return self.sums[row2][col2]-self.sums[row1-1][col2]
        else:
            return self.sums[row2][col2]+self.sums[row1-1][col1-1]-self.sums[row1-1][col2]-self.sums[row2][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```
## 324. Wiggle Sort II

Note: this is not a O(n) solution as wanted.

```
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop() 
        for i in range(0, len(nums), 2): nums[i] = arr.pop()
```

## 372. Super Pow
```
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # note that 1337 = 7*91, a product of two primes
        # We use Fermat's Little Thm and Chinese Reminder Thm 

        a = a % 1337
        b1, b2 = 0, 0
        for i in b:
            b1, b2 = (b1*10+i)%6, (b2*10+i)%190
        
        if a%7==0: r1 = 0
        else: r1 = (a**(b1))%7
        if a%191==0: r2 = 0
        else: r2 = (a**(b2))%191
            
        x1,x2 = 1, 1
        while (x1*191)%7 != 1:
            x1 += 1
        while (x2*7)%191 != 1:
            x2 += 1
        return (x1*191*r1+x2*7*r2)%1337
```
## 322. Coin Change

```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1]*(amount+1)
        dp[0] = 0
        for x in coins:
            if x <= amount:
                dp[x] = 1
        for i in range(1, amount+1):
            temp = [dp[i-x]+1 for x in coins if i-x >= 0  and dp[i-x]>=0]
            if temp: 
                dp[i] = min(temp)
        return dp[-1]
```
## 983. Minimum Cost For Tickets
```
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = {n:1 for n in days}
        dp = [0]*(days[-1]+1)
        for i in range(1,len(dp)):
            if i not in d:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0,i-1)]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
        return dp[-1]
```
## 368. Largest Divisible Subset

A O(n^2) DP solution:
```
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        dp = [0]*len(nums)
        nums.sort()
        dp[0] =[nums[0]]
        for i in range(1, len(nums)):
            temp = []
            for j in range(i):
                if len(dp[j]) > len(temp) and nums[i]%nums[j]==0:
                    temp = dp[j].copy()
            dp[i] = temp+[nums[i]]
        
        res = []
        for i in range(len(nums)):
            if len(dp[i]) > len(res):
                res = dp[i]
        return res

```
Same idea as above, but notice that we don't need to record the paths. We simply use `dp[i]` to record the length of the longest path ends at `nums[i]`.
```
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        dp = [0]*len(nums)
        nums.sort()
        dp[0] = 1
        for i in range(1, len(nums)):
            l = 0
            for j in range(i-1,-1, -1):
                if dp[j] > l and nums[i]%nums[j]==0:
                    l = dp[j]
            dp[i] = l+1
        
        max_length = max(dp)
        res, pos = [], dp.index(max_length)
        while max_length > 0:
            res.append(nums[pos])
            max_length -= 1
            if max_length == 0: break
                
            prev, pos = pos, dp.index(max_length)
            while nums[prev]%nums[pos] != 0:
                pos = dp.index(max_length, pos+1)
        return res[::-1]
```

## 139. Word Break

Brute-force recursive solution: 
```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {w:1 for w in wordDict}
        
        def dfs(s, d):
            if s == '': return True
            
            for i in range(len(s)):
                if s[:i+1] in d:
                    if dfs(s[i+1:], d):
                        return True
                    else: continue
            return False
        
        return dfs(s, d)
```

DP
```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {w:1 for w in wordDict}
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            for j in range(i, -1, -1):
                if dp[j] & (s[j:i] in d): 
                    dp[i] = 1
                    break
        return dp[-1]
```
## 143. Reorder List
Time O(n), space O(n) solution:

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        """
        if not head: return 
        
        deq = collections.deque()
        node = head
        while node:
            deq.append(node)
            node = node.next
        
        prev = deq.popleft()
        end = 1
        while deq:
            if end == 1:
                cur = deq.pop()
            else:
                cur = deq.popleft()
            prev.next, cur.next = cur, None
            prev = cur
            end = (end+1)%2
```
Time O(n), space O(1) solution:
```
# Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves
def _splitList(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        fast = fast.next

    middle = slow.next
    slow.next = None

    return head, middle

# Reverses in place a list.
# @return Returns the head of the new reversed list
def _reverseList(head):

  last = None
  currentNode = head

  while currentNode:
    nextNode = currentNode.next
    currentNode.next = last
    last = currentNode
    currentNode = nextNode

  return last

# Merges in place two lists
# @return The newly merged list.
def _mergeLists(a, b):

    tail = a
    head = a

    a = a.next
    while b:
        tail.next = b
        tail = tail.next
        b = b.next
        if a:
            a, b = b, a
            
    return head


class Solution:

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):

        if not head or not head.next:
            return

        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)
```
## 147. Insertion Sort List
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        
        sentinel = ListNode(float('-inf'))
        sentinel.next = head
        prev, cur = head, head.next
        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
            else:
                tmp_prev, tmp = sentinel, sentinel.next
                while tmp.val < cur.val:
                    tmp_prev, tmp = tmp, tmp.next
                prev.next = cur.next
                tmp_prev.next, cur.next = cur, tmp 
                cur = prev.next
        return sentinel.next
```
## 179. Largest Number

Remark: this is essentially a sorting problem. One just replaces the usual compare between two integers by a new partial order, thus the best solution is O(n lg n).
```
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ''
        nums = nums
        for i in range(1,len(nums)):
            cur = str(nums[i])
            j = i-1
            while j >= 0:
                temp = str(nums[j])
                if int(cur+temp) < int(temp+cur):
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    j -= 1
                else:
                    break
        for n in nums[::-1]:
            res += str(n)
        return res if res[0]!='0' else '0'
```
## 146. LRU Cache

```
class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.cnt = 0
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        else:
            self.cnt += 1
            self.store[key][1] = self.cnt 
            return self.store[key][0]

    def put(self, key: int, value: int) -> None:
        self.cnt += 1
        if len(self.store) == self.cap and key not in self.store:
            discard = min(self.store, key=lambda k:self.store[k][1] )
            del self.store[discard]
        
        self.store[key] = [value, self.cnt]
```

A much better solution is to use `collections.OrderedDict()`
```
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v   # set key as the newest one
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value
```

## 165. Compare Version Numbers

```
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2 = version1.split('.'), version2.split('.')
        for i in range(min(len(l1), len(l2))):
            if self.compare(l1[i],l2[i]) == 1: return 1
            elif self.compare(l1[i],l2[i]) == -1: return -1
            else:
                continue
        if len(l1) > len(l2) and any([int(l1[i])>0 for i in range(len(l2), len(l1))]):
            return 1  
        elif len(l1) < len(l2) and any([int(l2[i])>0 for i in range(len(l1), len(l2))]):
            return -1 
        else:
            return 0
    def compare(self, s1, s2):
        s1, s2 = str(int(s1)), str(int(s2))
        
        if int(s1) > int(s2): return 1
        elif int(s1) < int(s2): return -1
        else:
            return 0
```

## 150. Evaluate Reverse Polish Notation
```
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '/*+-':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(self.binaryCompute(int(n1),int(n2),tokens[i]))
            else:
                stack.append(tokens[i])
        
        return stack[0]
        
    def binaryCompute(self, n1, n2, op):
        
        if op == '*':
            return n1*n2
        elif op == '+':
            return n1+n2
        elif op == '-':
            return n1-n2
        else:
            q = n1/n2
            return math.floor(q) if q > 0 else math.ceil(q)
```

## 153. Find Minimum in Rotated Sorted Array
```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] <= nums[r]: return nums[l]
            
            mid = (l+r)//2
            if nums[mid] == nums[l]:
                return nums[r]
            elif nums[mid] > nums[l]:
                l = mid+1
            else:
                r = mid
```
## 152. Maximum Product Subarray

```
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        dp[0] = [nums[0],nums[0]]
        for i in range(1, len(nums)):
            temp1, temp2 = dp[i-1][0] * nums[i], dp[i-1][1] * nums[i]
            dp[i] = [min(temp1, temp2, nums[i]), max(temp1,temp2,nums[i])]
        return max(dp[i][1] for i in range(len(nums)))
```
## 151. Reverse Words in a String
```
class Solution:
    def reverseWords(self, s: str) -> str:
        vocab = s.split()
        res = ''
        for w in vocab[::-1]:
            res += ' '+w
        return res[1:]
```
## 187. Repeated DNA Sequences
```
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        
        history = {}
        res = []
        for i in range(9, len(s)):
            temp = s[i-9:i+1] 
            if temp in history and history[temp] == 1: 
                res.append(temp)
                history[temp] += 1
            else: history[temp] = history.get(temp,0)+1
        return res
```

## 208. Implement Trie (Prefix Tree)
```
class TrieNode:
    
    def __init__(self, s):
        self.children = {}
        self.value = s
        self.valid = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("")
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        for i in range(len(word)):
            if word[i] not in parent.children:
                node = TrieNode(word[:i+1])
                parent.children[word[i]] = node
            parent = parent.children[word[i]]
        parent.valid = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for l in word:
            if l not in parent.children:
                return False
            parent = parent.children[l]
        return parent.valid

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for l in prefix:
            if l not in parent.children:
                return False
            parent = parent.children[l]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
## 306. Additive Number
```
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3: return False
        
        for i in range(len(num)-2):
            for j in range(i+1, len(num)-1):
                s1, s2 = num[:i+1], num[i+1:j+1]
                if len(str(int(s2))) < j-i: break
                if self.checkAdditive(s1, s2, num, j+1): return True
        return False
        
    def checkAdditive(self, s1, s2, num, i):
        '''
        Check whether num[i:] satisfies the additive property, assuming the previous numbers are already known as strings s1 and s2
        '''
        while i < len(num):
            s3 = self.sum(s1, s2)
            if s3 != num[i:i+len(s3)]: return False
            else:
                i, s1, s2 = i+len(s3), s2, s3
        return True
        
        
    def sum(self, s1, s2):
        '''
        Given two strings of digits, return the sum as string (this would avoid overflow)
        '''
        if len(s1) > len(s2):
            s2 = '0'*(len(s1)-len(s2))+s2
        else:
            s1 = '0'*(len(s2)-len(s1))+s1
        
        additional, res = 0, ''
        for i in range(1, len(s2)+1):
            d1, d2 = int(s1[-i]), int(s2[-i])
            temp_sum = d1+d2+additional
            additional = temp_sum//10
            res = str(temp_sum%10)+res
                
        if additional == 1:
            return '1'+res
        else: 
            return res
```