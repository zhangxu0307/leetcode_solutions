# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inOreder(node, nodeList):
            if node.left != None:
                inOreder(node.left, nodeList)
            nodeList.append(node.val)
            if node.right != None:
                inOreder(node.right, nodeList)

        nodeList = []
        inOreder(root, nodeList)
        n = len(nodeList)
        absDiff = []
        for i in range(n-1):
            absDiff.append(nodeList[i+1]-nodeList[i])
        return min(absDiff)


root = TreeNode(1)
right1 = TreeNode(3)
left2 = TreeNode(2)
root.right = right1
right1.left = left2


s = Solution()
ans = s.getMinimumDifference(root)
print ans





