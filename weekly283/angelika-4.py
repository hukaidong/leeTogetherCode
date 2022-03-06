from collections import deque

class Solution:
    def kgcd(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if (a & 1) == 0 and (b & 1) == 0:
            return self.kgcd(a >> 1, b >> 1) << 1
        elif (b & 1) == 0:
            return self.kgcd(a, b >> 1)
        elif (a & 1) == 0:
            return self.kgcd(a >> 1, b)
        else:
            return self.kgcd(abs(a - b), min(a, b))
    
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        queued = deque(nums[1:])
        res = nums[0:1]
        
        while len(queued):
            val = queued.popleft()
            if val == 1 or res[-1] == 1:
                res.append(val)
                continue

            while len(res) and self.kgcd(res[-1], val) > 1:
                val = res[-1] * val // self.kgcd(res[-1], val)
                res.pop()

            res.append(val)
        
        return res
            