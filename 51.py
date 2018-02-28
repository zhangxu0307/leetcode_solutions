class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def isvalid(c, row, col):
            for i in range(row):
                if c[i] == col:
                    return False
                if abs(i-row)==abs(c[i]-col):
                    return False
            return True

        def dfs(c, result, row):
            if row == n:
                solution = []
                for i in range(n):
                    s = ["."]*n
                    print s
                    for j in range(n):
                        if c[i] ==  j:
                            s[j] = "Q"
                    s = "".join(s)
                    solution.append(s)
                result.append(solution)

            for i in range(n):
                flag = isvalid(c, row, i)
                if not flag:
                    continue
                c[row] = i
                dfs(c, result, row+1)

        c = [0*i for i in range(n)]
        result = []
        dfs(c, result, 0)
        return result

s = Solution()
n = 4
ans = s.solveNQueens(n)
print ans

