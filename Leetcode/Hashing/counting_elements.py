# Given an integer array arr, count how many elements x there are, 
# such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

class Solution:
    def countElements(self, arr: List[int]) -> int:
        ans = 0
        arr_set = set(arr)
        for n in arr:
            if n + 1 in arr_set:
                ans += 1
        return ans