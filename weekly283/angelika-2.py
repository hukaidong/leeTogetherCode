from collections import deque

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        ordered = deque([0] + nums)
        res = []
        num = ordered.popleft()
        if len(nums) == 0:
            return k * (k + 1) // 2
        
        while len(ordered) and k > 0:
            last, num = num, ordered.popleft()
            if (num > last + 1):
                high = min(num - 1, last + k)
                res.append((last + 1 + high) * (high - last) // 2)
                k -= high - last
                
        if k > 0:
            res.append((nums[-1] + 1 + nums[-1] + k) * k // 2)
        
        return sum(res)
            