from math import sqrt, floor

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        scan = dict()
        for circle in circles:
            x, y, r = circle
            for h in range(x - r, x + r + 1):
                v = floor(sqrt(r ** 2 - (x - h) ** 2))
                if h in scan:
                    scan[h].append((y - v, y + v))
                else:
                    scan[h] = [(y - v, y + v)]
            
        ans = 0
        for h, segs in scan.items():
            evt = dict()
            for st, ed in segs:
                evt[st] = (evt[st] if st in evt else []) + [1]
                evt[ed + 1] = (evt[ed + 1] if ed + 1 in evt else []) + [-1]
            last = min(evt.keys())
            cnt = sum(evt[last])
            for pos, ev in sorted(evt.items())[1:]:
                ans += pos - last if cnt > 0 else 0
                last = pos
                cnt += sum(ev)
        return ans