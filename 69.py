class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 1
        end = x
        mid = 0
        while start <= end:
            mid = (end + start)/2
            if x/mid == mid:
                return mid
            elif x/mid > mid:
                start = mid+1
            elif x/mid < mid:
                end = mid-1
        return end

x = 2
s = Solution()
ans = s.mySqrt(x)
print ans