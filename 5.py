class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def lenPalindrome(s, left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        if len(s) == 0:
            return ""
        n = len(s)
        maxlen = 0
        ansStr = ""
        for i in range(0, 2*n-1):
            right = i/2
            left = i/2
            if i%2 == 1:
                right += 1
            substr = lenPalindrome(s, left, right)
            if len(substr) > maxlen:
                ansStr = substr
                maxlen = len(substr)
        return ansStr

    def longestPalindrome2(self, s):

        if len(s) == 0:
            return ""

        n = len(s)
        maxlen = 0
        ans = ""
        isPalin = [[False for col in range(n)] for row in range(n)]
        print isPalin
        for i in range(0,n):
            for j in range(0,i):
                if s[i] == s[j] and (i-j <= 2 or isPalin[j+1][i-1]):
                    isPalin[j][i] = True
                    if i-j+1 > maxlen:
                        maxlen = i-j+1
                        ans = s[j:i+1]
        return ans






s = "baaba"
S = Solution()
ans = S.longestPalindrome2(s)
print ans