from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        a_set = set() 
        num_count_map = defaultdict(int)
        for num in nums:
            num_count_map[num] += 1
        uniques = [num for num, count in num_count_map.items() if count == 1]
        return max(uniques) if uniques else -1