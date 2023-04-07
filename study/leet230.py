# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def find(node, sort):
    if node.left:
        find(node.left, sort)
    sort.append(node.val)
    if node.right:
        find(node.right, sort)
    return

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sort = []
        find(root, sort)
        return sort[k-1]
