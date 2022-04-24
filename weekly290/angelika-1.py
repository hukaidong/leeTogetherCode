class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        cnts = dict()
        for arr in nums:
            for num in arr:
                cnts[num] = (cnts[num] if num in cnts else 0) + 1
        ans = []
        for key, val in cnts.items():
            if val == len(nums):
                ans.append(key)
        return sorted(ans)