
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

r0 =  TreeNode(1)
r1 =  TreeNode(2)
r2 =  TreeNode(3)
r3 =  TreeNode(4)
r4 =  TreeNode(5)

r0.left = r1
r0.right = r2
r1.right = r3
r3.left = r4

class Solution(object):
    def dfs(self,node,depth):
        if node.left == None and node.right == None:
            return depth
        d1 = d2 = 9999
        if node.left != None:
            d1 = self.dfs(node.left,depth+1)
        if node.right != None:
            d2 = self.dfs(node.right,depth+1)
        return min(d1,d2)
    def minDepth(self, root):
        return self.dfs(root,0)
s = Solution()
ans = s.minDepth(r0)
print ans
