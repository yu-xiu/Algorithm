# leetcode 2260. Minimum Consecutive Cards to Pick Up
# to solve this problem, 1) use sliding window 2) hash map
# equal to the find shortest distance between any two of the same element
# If we go through the array and use a hash map to record the indices for every element, 
# we can iterate over those indices to find the shortest distance.
#  For example, given cards = [1, 2, 6, 2, 1], we would map 1: [0, 4], 2: [1, 3], and 6: [2]. 
# Then we can iterate over the values and see that the minimum difference can be achieved from picking up the 2s.
from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)
            
        ans = float("inf")
        for key in dic:
            arr = dic[key]
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)
        
        return ans if ans < float("inf") else -1