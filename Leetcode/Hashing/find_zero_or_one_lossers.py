from collections import defaultdict
from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        seen = set()
        
        for w, l in matches:
            seen.add(w)
            seen.add(l)
            losses[l] += 1
        zero_losses = [p for p in seen if losses[p] == 0]
        one_losses = [p for p in seen if losses[p] == 1]
        
        zero_losses.sort()
        one_losses.sort()
        
        return [zero_losses, one_losses]