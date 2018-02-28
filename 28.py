class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == None:
            return -1
        if needle == None:
            return -1
        n1 = len(haystack)
        n2 = len(needle)
        if  n2 == 0:
            return 0
        elif n1 == 0:
            return  -1
        p1 = p2 = 0
        while p1 < n1:
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 = p1-p2+1
                p2 = 0
            if p2 == n2:
                return p1-n2
        else:
            return -1

hay = "mississippi"
needle = "issis"
s = Solution()
ans = s.strStr(hay, needle)
print ans