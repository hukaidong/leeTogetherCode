def minDeletion(self, nums: List[int]) -> int:
    cache = []
    pairs = 0
    for num in nums:
        if len(cache) == 0:
            cache.append(num)
        elif len(cache) == 1 and num != cache[-1]:
            cache.clear()
            pairs += 1

    return(len(nums) - pairs * 2)
