from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        need = Counter("balloon")
        have = Counter(text)
        return min(have[c] // need[c] for c in need)