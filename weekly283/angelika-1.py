class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        st, ed = s.split(":")
        r1, c1 = st
        r2, c2 = ed
        results = []

        for row in range(ord(r1), ord(r2) + 1):
            for col in range(int(c1), int(c2) + 1):
                results.append("%s%d" % (chr(row), col))

        return results
