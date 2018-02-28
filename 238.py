class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res1 = [1]*n
        res2 = [1]*n
        res = []
        for i in range(0, n-1):
            res1[i+1] = res1[i]*nums[i]
        print res1
        for i in range(n-1, 0, -1):
            res2[i-1] = res2[i]*nums[i]
        print res2
        for i in range(n):
            res.append(res1[i]*res2[i])
        return res

s = Solution()
nums = [1, 2, 3, 4]
ans = s.productExceptSelf(nums)
print ans