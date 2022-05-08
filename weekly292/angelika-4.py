# class Solution:
#     def hasValidPath(self, grid: List[List[str]]) -> bool:
from typing import List
from queue import Queue

def bfs(mp, r, c):
    que = Queue()
    visited = set()
    visited.add((1 if mp[0][0] == '(' else 0, 1 if mp[0][0] == ')' else 0, 1))
    visited.add((1 if mp[0][0] == '(' else 0, 1 if mp[0][0] == ')' else 0, -1))
    que.put((0, 0, 1 if mp[r - 1][c - 1] == '(' else 0, 1 if mp[r - 1][c - 1] == ')' else 0, 1))
    que.put((r - 1, c - 1, 1 if mp[r - 1][c - 1] == '(' else 0, 1 if mp[r - 1][c - 1] == ')' else 0, -1))
    while not que.empty():
        x, y, lp, rp, mask = que.get()
        if ((r + c - 1) // 2 - lp, (r + c - 1) // 2 - rp, -mask) in visited:
            print(r, c, x, y, lp, rp, mask)
            return True
        if lp + rp <= (r + c - 1) // 2 and x + 1 < r:
            new_st = (x + 1, y, lp + (1 if mp[x + 1][y] == '(' else 0), rp + (1 if mp[x + 1][y] == ')' else 0), mask)
            if not (lp + (1 if mp[x + 1][y] == '(' else 0), rp + (1 if mp[x + 1][y] == ')' else 0), mask) in visited:
                if (lp + (1 if mp[x + 1][y] == '(' else 0) - rp - (1 if mp[x + 1][y] == ')' else 0)) * mask >= 0:
                    visited.add((lp + (1 if mp[x + 1][y] == '(' else 0), rp + (1 if mp[x + 1][y] == ')' else 0), mask))
                    que.put(new_st)

        if lp + rp <= (r + c - 1) // 2 and y + 1 < c:
            new_st = (x, y + 1, lp + (1 if mp[x][y + 1] == '(' else 0), rp + (1 if mp[x][y + 1] == ')' else 0), mask)
            if not (lp + (1 if mp[x][y + 1] == '(' else 0), rp + (1 if mp[x][y + 1] == ')' else 0), mask) in visited:
                if (rp + (1 if mp[x][y + 1] == ')' else 0) - lp - (1 if mp[x][y + 1] == '(' else 0)) * mask <= 0:
                    visited.add((lp + (1 if mp[x][y + 1] == '(' else 0), rp + (1 if mp[x][y + 1] == ')' else 0), mask))
                    que.put(new_st)

    return False

def hasValidPath(grid: List[List[str]]) -> bool:
    r, c = len(grid), len(grid[0])
    if (r + c) & 1 < 1:
        return False
    return bfs(grid, r, c)

print(hasValidPath([[")",")"],["(","("]]))
print(hasValidPath([["(","("],[")",")"]]))
print(hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]))