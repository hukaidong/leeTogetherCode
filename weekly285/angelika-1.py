class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        high, low = [], []
        res = 0
        for num in nums:
            if len(high) and num < high[-1]:
                res += 1 if len(high) > 1 else 0
                high = [num]
            elif len(high) < 1 or num > high[-1]:
                high.append(num)
                
            if len(low) and num > low[-1]:
                res += 1 if len(low) > 1 else 0
                low = [num]
            elif len(low) < 1 or num < low[-1]:
                low.append(num)
            
        return res