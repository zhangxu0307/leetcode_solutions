class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def similarity(s):
            upperflag = True
            lowerFlag = True
            for ch in s:
                upperflag = ch.isupper() and upperflag
                lowerFlag &= ch.islower() and lowerFlag
            return upperflag, lowerFlag

        if word[0].isupper():
            uflag, lflag = similarity(word[1:])
            if uflag or lflag:
                return True
            else:
                return False
        else:
            uflag, lflag = similarity(word)
            if lflag:
                return True
            else:
                return False

s = Solution()
ans = s.detectCapitalUse("Abc")
print ans