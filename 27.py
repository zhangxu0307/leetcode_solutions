class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        def swap(nums, i1, i2):
            tmp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = tmp

        n = len(nums)
        start = 0
        end = n-1
        while start <= end:

            if nums[start] == val and nums[end] != val:
                swap(nums,start, end)
                start += 1
                end -= 1
            elif nums[start] == val and nums[end] == val:
                end -= 1
            else:
                start += 1
        return start


nums = [3, 2, 2, 3, 5, 1, 3]
s = Solution()
ans = s.removeElement(nums,3)
print nums
print ans
