class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        minLoc = nums[0]
        maxLoc = nums[0]
        globalMax = nums[0]
        for i in range(1, n):
            tmp = minLoc
            minLoc = min(min(nums[i] * maxLoc, nums[i]), nums[i] * minLoc)
            maxLoc = max(max(nums[i] * maxLoc, nums[i]), nums[i] * tmp)
            globalMax = max(globalMax, maxLoc)

        return globalMax

s = Solution()
nums = [2,3,-2,4]
ans = s.maxProduct(nums)
print ans

