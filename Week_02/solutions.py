#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)
        if set_s == set_t:
            for i in set_s:
                if s.count(i) != t.count(i): return False
        else:
            return False
        return True

# @lc code=end


#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            d[n] = i

# @lc code=end


#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: 'Node', res: List):
        if root:
            res.append(root.val)
            for i in root.children:
                self.helper(i, res)
        
# @lc code=end


#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            k = tuple(sorted(i))
            d[k] = d.get(k, []) + [i]
        return list(d.values())

# @lc code=end


#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: TreeNode, res: List):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

# @lc code=end


#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: TreeNode, res: List):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
            
# @lc code=end


#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res, heap = [], []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for key, val in freq.items():
            heapq.heappush(heap, [val, key])  # 默认小顶堆
            if len(heap) > k: heapq.heappop(heap)
        while len(heap):
            res.append(heap[0][1])
            heapq.heappop(heap)
        return res[::-1]

# @lc code=end


#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        old = {1, }
        nums = []
        heap = []
        heapq.heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heapq.heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                next_ugly = curr_ugly * i
                if next_ugly not in old:
                    old.add(next_ugly)
                    heapq.heappush(heap, next_ugly)

        return nums[n - 1]

# @lc code=end


