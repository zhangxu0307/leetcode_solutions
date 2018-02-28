class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i1,i2):
            tmp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = tmp

        def reverse(nums, start, end):
            while start < end:
                swap(nums, start, end)
                start += 1
                end -= 1

        n = len(nums)
        i = n-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = n-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            swap(nums, i, j)
        reverse(nums, i+1, n-1)


nums = [1,3,2]
s = Solution()
ans = s.nextPermutation(nums)
print nums

