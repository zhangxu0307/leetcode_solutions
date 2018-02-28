class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        d = {}
        num = len(candies)
        for i in range(num):
            d[candies[i]] = 1
        kindNum = len(d)
        if kindNum > num/2:
            return num/2
        else:
            return kindNum

s = Solution()
candies = [1,1,2,2,3,4]
ans = s.distributeCandies(candies)
print ans
