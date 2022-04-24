class MultiSet:
    def __init__(self):
        self.data = dict()
    
    def add(self, val):
        if val in self.data:
            self.data[val] += 1
        else:
            self.data[val] = 1
    
    def remove(self, val):
        if not val in self.data:
            return
        if self.data[val] == 1:
            del self.data[val]
        else:
            self.data[val] -= 1
    
    def not_less_than(self, threshold):
        cnt = 0
        for key, val in self.data.items():
            if key >= threshold:
                cnt += val
        return cnt

def add_event(evts, pos, val):
    if pos in evts:
        evts[pos].append(val)
    else:
        evts[pos] = [val]
    
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        evts = dict()
        for rect in rectangles:
            wi, hi = rect
            add_event(evts, 0, hi)
            add_event(evts, wi + 1, -hi)
        
        queries = dict()
        for qx, qy in points:
            add_event(queries, qx, qy)
            add_event(evts, qx, 0)
        
        heights = MultiSet()
        events = list(sorted(evts.items()))
        for val in events[0][1]:
            heights.add(val)
        
        results = dict()
        for pos, evt in events[1:]:
            for ev in evt:
                heights.remove(abs(ev))
            for qy in queries[pos] if pos in queries else []:
                results[(pos, qy)] = heights.not_less_than(qy)
        
        return [results[(qx, qy)] if (qx, qy) in results else 0 for qx, qy in points]