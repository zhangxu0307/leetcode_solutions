class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        for i in range(n-2, -1, -1):
            l = len(triangle[i])
            print l
            for j in range(l):
                triangle[i][j] = min(triangle[i+1][j+1]+triangle[i][j], triangle[i+1][j]+triangle[i][j])

        return triangle[0][0]


s = Solution()
t =[
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
ans = s.minimumTotal(t)
print ans