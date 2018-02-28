class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        def dfs(nums, ans, path):
            if not nums:
                ans.append(path)
            else:
                d = {}
                for i in xrange(len(nums)):
                    if nums[i] not in d:
                        dfs(nums[:i]+nums[i+1:], ans, path+[nums[i]])
                        d[nums[i]] = 1
        nums.sort()
        dfs(nums, ans, [])
        return ans

nums = [1,1,2,3]
s = Solution()
ans = s.permuteUnique(nums)
print ans
