#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root # 不再下探的终止条件
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root # 在左右子树中分别找到了一个节点
        
# @lc code=end


#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return
        root = TreeNode(None)
        root.val = preorder[0]
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1 + index], inorder[:index])
        root.right = self.buildTree(preorder[1 + index:], inorder[1 + index:])
        return root
        
# @lc code=end


#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(index, level, state):
            if level > k:
                res.append(state)
                return

            for i in range(index, n + 1):
                helper(i + 1, level + 1, state + [i])

        helper(1, 1, [])
        return res
        
# @lc code=end


#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:      
        res = []
        old = set()

        def helper(level, state):
            if level > len(nums):
                res.append(state)
                return

            for i in range(len(nums)):
                if i in old:
                    continue
                old.add(i)
                helper(level + 1, state + [nums[i]])
                old.remove(i)
            return

        helper(1, [])
        return res

# @lc code=end

