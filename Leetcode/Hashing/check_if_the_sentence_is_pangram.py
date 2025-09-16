# A pangram is a sentence where every letter of the English alphabet appears at least once.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) >= 26
        