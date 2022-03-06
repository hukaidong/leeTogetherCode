from typing import Dict
class Solution:
    def countLetter(self, word: str) -> Dict[str, int]:
        cnt = dict();
        for letter in word:
            if letter in cnt:
                cnt[letter] += 1
            else:
                cnt[letter] = 1
        return cnt
                
    def compare(self, d1: Dict[str, int], d2: Dict[str, int]) -> int:
        res = 0
        for k, v in d2.items():
            res += max(v - (d1[k] if k in d1 else 0), 0)
        return res
        
    def minSteps(self, s: str, t: str) -> int:
        d1, d2 = self.countLetter(s), self.countLetter(t)
        return self.compare(d1, d2) + self.compare(d2, d1)
        pass