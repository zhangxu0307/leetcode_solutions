class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import copy
        ans = []
        candidates.sort()

        def dfs(tryList, start):
            if sum(tryList) == target:
                ans.append(tryList)
                return
            elif sum(tryList) > target:
                return

            for i in range(start, len(candidates)):
                if i != start and candidates[i] == candidates[i - 1]:
                    continue
                dfs(tryList+[candidates[i]], i+1)

        dfs([], 0)
        return ans

candidates = [29,19,14,33,11,5,9,23,23,33,12,9,25,25,12,21,14,11,20,30,17,19,5,6,6,5,5,11,12,25,31,28,31,33,27,7,33,31,17,13,21,24,17,12,6,16,20,16,22,5]
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
s = Solution()
ans = s.combinationSum2(candidates, target)
print ans

