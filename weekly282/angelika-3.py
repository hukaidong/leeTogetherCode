from functools import reduce
from operator import __add__
class Solution:
    def test(self, period: int, time: List[int], totalTrips: int) -> bool:
        return reduce(__add__, map(lambda t: period // t, time)) >= totalTrips
        pass
    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low, high = 1, max(time) * totalTrips
        while low < high:
            mid = (low + high) >> 1
            if self.test(mid, time, totalTrips):
                high = mid
            else:
                low = mid + 1
        return low