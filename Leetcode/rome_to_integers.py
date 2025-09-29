class Solution:
    def romanToInt(self, s: str) -> int:
        values_map = {'M' : 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I' : 1}
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and values_map[s[i]] < values_map[s[i + 1]]:
                total += values_map[s[i + 1]] - values_map[s[i]]
                i += 2
            else:
                total += values_map[s[i]]
                i += 1
        return total
