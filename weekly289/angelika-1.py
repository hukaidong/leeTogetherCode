class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            output = []
            for pos in range((len(s) + k - 1) // k):
                sub = s[pos * k:min(len(s), pos * k + k)]
                output.append(str(sum(int(ch) for ch in sub)))
            s = ''.join(output)
        return s