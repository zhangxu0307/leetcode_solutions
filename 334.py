class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        minNum1 = 9999999999999
        minNum2 = 9999999999999
        for i in range(0, len(nums)):
            if nums[i] <= minNum1:
                minNum1 = nums[i]
            elif nums[i] <= minNum2:
                minNum2 = nums[i]
            else:
                return True
        return False

s = Solution()
nums = [3,2,1,5,6,7]
ans = s.increasingTriplet(nums)
print ans