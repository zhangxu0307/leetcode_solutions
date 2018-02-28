class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        ans = ""
        index = 0
        flag = True
        if n < 2*k and n > k:
            ans = s[:k][::-1]+s[k:]
        else:
            while index < n:
                if flag == True:
                    ans += s[index:index+k][::-1]
                else:
                    ans += s[index:index+k]
                flag = not flag
                index += k
        return ans


s = "abcdefgh"
k = 3
ss = Solution()
ans = ss.reverseStr(s, k)
print ans