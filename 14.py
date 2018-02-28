#encoding=utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strNum = len(strs)
        if strNum == 0:
            return ""
        minlen = min([len(sstr) for sstr in strs])
        if minlen == 0:
            return ""
        prefix = []
        flag = False
        for i in range(minlen):
            for j in range(strNum):
                if j == 0:
                    flag = True
                    ch = strs[j][i]
                else:
                    if strs[j][i] == ch:
                        flag = True
                    else:
                        flag = False
                        break
            if flag == True:
                prefix.append(ch)
            else:
                break
        return "".join(prefix)

    def longestCommonPrefix2(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        prefix = strs[0] # 取第一个字符串作为搜索基础
        for i in range(1, n):
            while strs[i].find(prefix) != 0: # 寻找子串，位置不是从0开始或者没找大返回了-1
                prefix = strs[0][0:len(prefix)-1]
                if len(prefix) == 0: # 找到最好没有公共前缀
                    return ""
        return prefix

    def commonPrefix(self,strLeft, strRight): # 寻找两个字符串的公共前缀
        minLen = min(len(strLeft), len(strRight))
        for i in range(minLen):
            if strLeft[i] != strRight[i]:
                return strLeft[:i]
        return strLeft[:minLen]

    def findPrefix(self, strs, left, right): # 分治法求公共前缀
        if left == right:
            return strs[left]
        else:
            mid = (left+right)/2
            lcpleft = self.findPrefix(strs, left, mid)
            lcpright = self.findPrefix(strs, mid+1, right)
            return self.commonPrefix(lcpleft, lcpright)

    def longestCommonPrefix3(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        return self.findPrefix(strs, 0, n-1)










str1 = "abc"
str2 = "abcd"
str3 = "abce"
#strs = [str1, str2, str3]
strs = ["","acc","ccc"]
s = Solution()
ans = s.longestCommonPrefix3(strs)
print ans