# counting

# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, 
# return the list of integers that are present in each array of nums sorted in ascending order.

# count frequency of the occurance of the ints in nums[i]
from collections import Counter
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = Counter()
        for arr in nums:
            counter.update(arr)
        result = []
        for n, cnt in counter.items():
            if cnt == len(nums):
                result.append(n)
        return sorted(result)