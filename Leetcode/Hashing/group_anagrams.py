# if two strings are anagrams, they are equal after both being sorted
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # 当访问一个不存在的键时，自动创建一个空列表[] 作为该键的默认值，并返回它
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())