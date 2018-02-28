class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = s.split()
        if len(ans) != 0:
            return len(ans[-1])
        else:
            return 0

string = ""
s = Solution()
ans = s.lengthOfLastWord(string)
print ans
