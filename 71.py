class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        paths = [p for p in path.split("/") if p != "." and p != ""]
        print paths
        stack = []
        for p in paths:
            if p == "..":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/"+"/".join(stack)

path = "/a/./b/../../c/"
s = Solution()
ans = s.simplifyPath(path)
print ans
