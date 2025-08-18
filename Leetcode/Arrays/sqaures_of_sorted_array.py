from typing import List
"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
"""
class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        nums = [x * x for x in nums]
        return sorted(nums)