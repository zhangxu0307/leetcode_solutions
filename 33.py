class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums, start, end):

            while start <= end and start >= 0 and end < len(nums):
                mid = (start + end) / 2
                if nums[mid] > target:
                    end = mid-1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    return mid
            else:
                return -1
        n = len(nums)
        if n == 0:
            return -1
        axis = 0
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                axis = i-1
                break
        ans = binarySearch(nums, 0, axis)
        ans2 = binarySearch(nums, axis+1, n-1)
        print ans, ans2
        if ans != -1:
            return ans
        elif ans2 != -1:
            return ans2
        else:
            return -1





nums = [4,5,6,7,0,1,2]
#nums = [3,1]
target = 4
s = Solution()
ans = s.search(nums, target)
print ans