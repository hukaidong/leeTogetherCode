def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    dis1 = set(nums1)
    dis2 = set(nums2)

    return [list(dis1 - dis2), list(dis2 - dis1)]
