class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        len_pref = len(pref)
        for word in words:
            if len(word) >= len_pref and word[0:len_pref] == pref:
                result += 1
        return result