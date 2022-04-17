class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        r2 = [[0 for y in range(m)] for x in range(n)]
        r5 = [[0 for y in range(m)] for x in range(n)]
        c2 = [[0 for x in range(n)] for y in range(m)]
        c5 = [[0 for x in range(n)] for y in range(m)]
        fives = []

        for r in range(n):
            for c in range(m):
                val = grid[r][c]
                if val % 5 == 0:
                    fives.append((r, c))
                while val % 5 == 0:
                    val //= 5
                    r5[r][c] += 1
                    c5[c][r] += 1
                while (val & 1) == 0:
                    val >>= 1
                    r2[r][c] += 1
                    c2[c][r] += 1

        for r in range(1, n):
            for c in range(m):
                c2[c][r] += c2[c][r - 1]
                c5[c][r] += c5[c][r - 1]

        for c in range(1, m):
            for r in range(n):
                r2[r][c] += r2[r][c - 1]
                r5[r][c] += r5[r][c - 1]

        ans = 0
        for r in range(n):
            for c in range(m):
                up5 = c5[c][r - 1] if r > 0 else 0
                up2 = c2[c][r - 1] if r > 0 else 0
                down5 = c5[c][n - 1] - c5[c][r]
                down2 = c2[c][n - 1] - c2[c][r]
                left5 = r5[r][c - 1] if c > 0 else 0
                left2 = r2[r][c - 1] if c > 0 else 0
                right5 = r5[r][m - 1] - r5[r][c]
                right2 = r2[r][m - 1] - r2[r][c]
                cur5 = r5[r][c] - (r5[r][c - 1] if c > 0 else 0)
                cur2 = r2[r][c] - (r2[r][c - 1] if c > 0 else 0)
                ans = max(ans, min(left5 + cur5 + up5, left2 + cur2 + up2))
                ans = max(ans, min(left5 + cur5 + down5, left2 + cur2 + down2))
                ans = max(ans, min(right5 + cur5 + up5, right2 + cur2 + up2))
                ans = max(ans, min(right5 + cur5 + down5, right2 + cur2 + down2))
                ans = max(ans, min(r5[r][m - 1], r2[r][m - 1]))
                ans = max(ans, min(c5[c][n - 1], c2[c][n - 1]))

        return ans
