
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def opt(i, j, memoized=None):
            if i < 0 or j < 0 or i >= m or j >= n:
                return float('inf')
            elif i == 0 and j == 0:
                return grid[i][j]
            memoized = memoized or [[None for _j in range(n)] for _i in range(m)]
            if memoized[i][j] is None:
                memoized[i][j] = grid[i][j] + min(opt(i - 1, j, memoized), opt(i, j - 1, memoized))
            return memoized[i][j]
        return opt(m - 1, n - 1)
    