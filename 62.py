class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        d = [[0 for i in range(n)] for i in range(m)]
        d[0][0] = 1
        for i in range(1, m):
            d[i][0] = 1
        for i in range(1, n):
            d[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j]+d[i][j-1]
        return d[-1][-1]

m = 5
n = 0
s = Solution()
ans = s.uniquePaths(m, n)
print ans