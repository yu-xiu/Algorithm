from typing import List

"""
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""
class Solution:
    def longest_ones(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        max_ones = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
                
            max_ones = max(max_ones, right - left + 1)
            
        return max_ones