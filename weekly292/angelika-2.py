class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        pass

def traverse(node, res):
    agg = (node.val, 1)
    if node.left is not None:
        sum_c, cnt = traverse(node.left, res)
        agg = (agg[0] + sum_c, agg[1] + cnt)

    if node.right is not None:
        sum_c, cnt = traverse(node.right, res)
        agg = (agg[0] + sum_c, agg[1] + cnt)

    if agg[0] // agg[1] == node.val:
        res['cnt'] += 1

    return agg

def averageOfSubtree(root):
    res = {"cnt": 0}
    traverse(root, res)
    return res['cnt']

print(averageOfSubtree(TreeNode(3, None, None)))
print(averageOfSubtree(TreeNode(3, TreeNode(1, None, None), TreeNode(5, None, None))))
print(averageOfSubtree(TreeNode(3, TreeNode(1, None, None), TreeNode(5, TreeNode(2, None, None), None))))
print(averageOfSubtree(TreeNode(3, TreeNode(1, None, None), TreeNode(5, TreeNode(2, None, None), TreeNode(4, None, None)))))