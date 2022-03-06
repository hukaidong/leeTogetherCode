# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findRoot(self, parent, val):
        if not val in parent or parent[val] == val:
            return val
        else:
            parent[val] = self.findRoot(parent, parent[val])
            return parent[val]

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        parent = dict()

        for desc in descriptions:
            pa, ch, isLeft = desc
            if not(pa in nodes):
                nodes[pa] = TreeNode(pa)

            if not(ch in nodes):
                nodes[ch] = TreeNode(ch)

            if isLeft:
                nodes[pa].left = nodes[ch]
                parent[ch] = self.findRoot(parent, pa)
            else:
                nodes[pa].right = nodes[ch]
                parent[ch] = self.findRoot(parent, pa)

        rootVal = self.findRoot(parent, descriptions[-1][1])
        return nodes[rootVal]
