class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        idx = 0
        cav = dict()
        cnt = dict()
        for r1, c1, r2, c2 in artifacts:
            cnt[idx] = (r2 - r1 + 1) * (c2 - c1 + 1)
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    cav[(r, c)] = idx
            idx += 1
        
        ans = 0
        for x, y in dig:
            if (x, y) in cav:
                no_a = cav[(x, y)]
                cnt[no_a] -= 1
                if cnt[no_a] == 0:
                    ans += 1
        
        return ans