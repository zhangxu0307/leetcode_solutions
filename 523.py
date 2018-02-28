class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        sumNum = 0
        mod = {}
        mod[0] = -1
        for i in range(n):
            sumNum += nums[i]
            if k != 0:
                sumNum %= k
                if sumNum in mod:
                    if i-mod[sumNum] > 1:
                        return True
                else:
                    mod[sumNum] = i
            else:
                if sumNum == 0 and i >= 1:
                    return True
        return False

nums = [0, 0]
s = Solution()
ans = s.checkSubarraySum(nums, 0)
print ans
