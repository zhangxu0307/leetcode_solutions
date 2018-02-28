class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        import copy
        def isPalindrome(testStr):
            start = 0
            end = len(testStr)-1
            while (start <= end and testStr[start] == testStr[end]):
                start += 1
                end -= 1
            return start >= end

        def dfs(s, path, result, start):
            if start == len(s):
                result.append(copy.deepcopy(path))
                return
            for i in range(start, len(s)):

                substr = s[start:i+1]
                flag = isPalindrome(substr)
                if flag:
                    path.append(substr)
                    dfs(s, path, result, i+1)
                    path.pop(-1)

        path = []
        result = []
        dfs(s, path, result, 0)
        return result

s = Solution()
ss = "aaab"
ans = s.partition(ss)
print ans