
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        res = 0
        for num in nums:
            d[num] = 1
        for i in nums:
            length = 1
            j = i-1
            while d.has_key(j):
                del d[j]
                j -= 1
                length += 1
            k = i+1
            while d.has_key(k):
                del d[k]
                k += 1
                length += 1
            res = max(res, length)
        return res

s = Solution()
nums = [100, 4, 200, 1, 3, 2]
ans = s.longestConsecutive(nums)
print ans





