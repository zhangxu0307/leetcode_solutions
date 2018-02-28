class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        d = [[0 for i in range(n)] for i in range(m)]
        print d
        d[0][0] = grid[0][0]
        for i in range(1, n):
            d[0][i] = d[0][i-1]+grid[0][i]
        for i in range(1, m):
            d[i][0] = d[i-1][0]+grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = min(d[i-1][j]+grid[i][j], d[i][j-1]+grid[i][j])
        print d
        return d[-1][-1]


grid = [[1,2,5],[3,2,1]]
s = Solution()
ans = s.minPathSum(grid)
print ans