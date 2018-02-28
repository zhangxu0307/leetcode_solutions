class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index, num in enumerate(nums):
            other = target-num
            if not d.has_key(other):
                d[num] = index
            else:
                return [d[other], index]

s = Solution()
nums = [2, 7, 11, 15]
target = 9
ans = s.twoSum(nums, target)
print ans
