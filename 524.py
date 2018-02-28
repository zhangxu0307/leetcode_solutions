class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            i = 0
            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1
            if i == len(word):
                return word
        return ""

s1 = "abpcplea"
d = ["ale","apple","monkey","plea"]
s = Solution()
ans = s.findLongestWord(s1,d)
print ans
