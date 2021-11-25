# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sub_search(self, cur, deep, ans):
        if cur == None:
            return
        if len(ans) < deep + 1:
            ans.append(float('-inf'))
        if ans[deep] < cur.val:
            ans[deep] = cur.val
        self.sub_search(cur.left, deep + 1, ans)
        self.sub_search(cur.right, deep + 1, ans)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        ans = []
        ans.append(root.val)
        self.sub_search(root.left, 1, ans)
        self.sub_search(root.right, 1, ans)
        return ans