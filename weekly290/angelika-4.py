def add_event(evts, pos, val):
    if pos in evts:
        evts[pos].append(val)
    else:
        evts[pos] = [val]

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        evts = dict()
        for st, ed in flowers:
            add_event(evts, st, 1)
            add_event(evts, ed + 1, -1)
            
        queries = dict()
        for per in persons:
            add_event(evts, per, 0)
            queries[per] = 0
            
        cnt = 0
        for pos, evt in sorted(evts.items()):
            cnt += sum(evt)
            if pos in queries:
                queries[pos] = cnt
        
        return [queries[person] for person in persons]