class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s) #转成list 让string s可修改
        i = 0
        j = len(s) - 1
        while i < j:
            if not chars[i].isalpha():
                i += 1
            elif not chars[j].isalpha():
                j -= 1
            else:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return ''.join(chars)