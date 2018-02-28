class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.counter = 0

        def isvalid(c, row, col):
            for i in range(row):
                if c[i] == col:
                    return False
                if abs(i-row) == abs(c[i]-col):
                    return False
            return True

        def dfs(c, row):
            if row == n:
                self.counter += 1
            for i in range(n):
                flag = isvalid(c, row, i)
                if not flag:
                    continue
                c[row] = i
                dfs(c, row+1)

        c = [0*i for i in range(n)]
        counter = 0
        dfs(c, 0)
        return self.counter

s = Solution()
ans = s.totalNQueens(4)
print ans


