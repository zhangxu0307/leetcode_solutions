class Solution(object):
    # def threeSumClosest(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     d = {}
    #     minNum = 99999
    #     for i,num in enumerate(nums):
    #         for j,otherNum in enumerate(nums[i+1:]):
    #             if otherNum not in d:
    #                 d[target-otherNum-num] = i+j
    #             elif d[otherNum] != i+j:
    #                 return [num, target-num-otherNum, otherNum]
    #     print d

    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        minNum = 9999999
        for i in range(n):
            start = i+1
            end = n-1
            while start < end:
                tmp = nums[i]+nums[start]+nums[end]-target
                if abs(tmp) < abs(minNum):
                    minNum = tmp
                if minNum == 0:
                    return target
                elif tmp < 0:
                    start += 1
                elif tmp > 0:
                    end -= 1
        return minNum+target




#nums = [-1, 2, 1, -4]
nums = [0,2,1,-3]
t = 1
s = Solution()
ans = s.threeSumClosest(nums, t)
print ans
