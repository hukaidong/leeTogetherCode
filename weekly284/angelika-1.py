class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        loc = []
        for idx in range(len(nums)):
            if nums[idx] == key:
                loc.append(idx)

        res = []
        pt, ch = 0, 0
        while pt < len(nums) and ch < len(loc):
            while pt < len(nums) and pt < loc[ch] - k:
                pt += 1
            res.append(pt)
            pt += 1
            if pt > loc[ch] + k:
                ch += 1

        return res
