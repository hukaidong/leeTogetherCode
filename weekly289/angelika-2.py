class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = dict()
        for task in tasks:
            cnt[task] = 1 + (cnt[task] if task in cnt else 0)
        ans = 0
        for key, val in cnt.items():
            if val == 1 or val % 2 > 0 and (val - 3) % 2 > 0:
                return -1
            ans += min((val + 2) // 3, val // 3 + (val % 3 + 1) // 2)
        return ans